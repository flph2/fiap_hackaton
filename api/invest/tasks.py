# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import pandas as pd
import numpy as np
import scipy.sparse as sps


def dataPredict(data):
    """
    Task para rodar o modelo existente
    nos dados recebidos via formulario
    """
    userid = data['userid']
    idade = data['idade']
    perfilInvestidor = data['perfilInvestidor']
    scoreSituacaoFinanceira = data['scoreSituacaoFinanceira']
    scoreNivelConhecimento = data['scoreNivelConhecimento']

    df = pd.DataFrame.from_dict(
        {
            userid: [
                idade,
                perfilInvestidor,
                scoreSituacaoFinanceira,
                scoreNivelConhecimento,
            ]
        },
        orient='index',
        columns=[
            'idade',
            'perfilinvestidor',
            'scoresituacaofinanceira',
            'scorenivelconhecimento'
        ]
    )
    # Cria classes
    df['idade'] = pd.cut(
        df['idade'],
        bins=[0, 20, 35, 65, 100],
        labels=[
            "jovem",
            "jovemadulto",
            "adulto",
            "idoso"
        ]
    )

    df.loc[:, 'perfilinvestidor'] = 'perfil' + df['perfilinvestidor'].map(str)
    df.loc[:, 'scoresituacaofinanceira'] = 'scoresf' + df['scoresituacaofinanceira'].map(str)  # noqa
    df.loc[:, 'scorenivelconhecimento'] = 'scorenc' + df['scorenivelconhecimento'].map(str)  # noqa

    for index, rows in df.iterrows():
        features = [rows.idade, rows.perfilinvestidor, rows.scoresituacaofinanceira, rows.scorenivelconhecimento]

    resultado = new_user_recommendation(features)

    # Save Result
    from invest.models import Result
    ret = Result(ClienteId=data['userid'], Resultado=resultado)
    ret.save()


def new_user_recommendation(
        new_user_features,
        nrec_items=5):
    import pickle
    model = pickle.load(open('/data/models/lightfm', 'rb'))
    item_features = pickle.load(open('/data/models/item_features', 'rb'))
    item_id_map = pickle.load(open('/data/models/item_id_map', 'rb'))
    interactions = pickle.load(open('/data/models/interactions', 'rb'))
    user_feature_map = pickle.load(open('/data/models/user_feature_map', 'rb'))
    item_dict = item_id_map

    target_indices = []
    for feature in new_user_features:
        target_indices.append(user_feature_map[feature])

    features = np.zeros(len(user_feature_map.keys()))
    for i in target_indices:
        features[i] = 1
    features = sps.csr_matrix(features)

    n_users, n_items = interactions.shape
    scores = pd.Series(model.predict(0, np.arange(8603),
                                     user_features=features, item_features=item_features))  # noqa
    scores.index = list(item_id_map.values())
    scores = list(pd.Series(scores.sort_values(ascending=False).index))

    return_score_list = scores[0:nrec_items]
    inv_item_id_map = {v: k for k, v in item_dict.items()}
    scores = list(pd.Series(return_score_list).apply(lambda x: inv_item_id_map[x]))  # noqa

    ret = []
    counter = 1
    for i in scores:
        ret.append(str(counter) + '- ' + str(i))
        counter += 1

    return ret

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

def dataPredict(data):
    """
    Task para rodar o modelo existente
    nos dados recebidos via formulario
    """
    from invest.models import Result
    data_id = data['dataId']
    cliente_id = data['ClienteId']
    idade = data['Idade']
    estado_civil = data['EstadoCivil']

    resultado = modelo(
        data_id,
        cliente_id,
        idade,
        estado_civil
    )
    ret = Result(ClienteId=cliente_id, Resultado=resultado)
    ret.save()
    return ret


def modelo(*args):
    #  TODO : Implementar modelo
    teste = []
    teste.append('Renda fixa com liquidez diaria 1')
    teste.append('Renda fixa com liquidez diaria 2')
    teste.append('Renda fixa com liquidez diaria 3')
    teste.append('Renda fixa com liquidez diaria 4')
    return teste

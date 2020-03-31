# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from invest.tasks import dataPredict


class Predict(models.Model):
    """
    Model utilizado para predizer os investimentos
    do usuario
    """
    userid = models.IntegerField()
    idade = models.IntegerField()
    perfilInvestidor = models.IntegerField()
    scoreSituacaoFinanceira = models.FloatField()
    scoreNivelConhecimento = models.FloatField()


@receiver(post_save, sender=Predict, dispatch_uid="predict")  # noqa
def predict_task(sender, instance, **kwargs):
    """
    Método responsavel por instanciar a task
    para predizer investimentos do ususario
    """
    data = {
        'userid': instance.userid,
        'idade': instance.idade,
        'perfilInvestidor': instance.perfilInvestidor,
        'scoreSituacaoFinanceira': instance.scoreSituacaoFinanceira,
        'scoreNivelConhecimento': instance.scoreNivelConhecimento,
    }
    ret = dataPredict(data)
    return ret


class Result(models.Model):
    """
    Model com resultado da predicao
    """
    ClienteId = models.CharField(max_length=100)
    Resultado = models.TextField()

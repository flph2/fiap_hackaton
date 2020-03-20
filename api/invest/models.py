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
    dataId = models.CharField(max_length=100)
    ClienteId = models.CharField(max_length=100)
    Idade = models.CharField(max_length=100)
    EstadoCivil = models.CharField(max_length=100)


@receiver(post_save, sender=Predict, dispatch_uid="predict")  # noqa
def predict_task(sender, instance, **kwargs):
    """
    Método responsavel por instanciar a task
    para predizer investimentos do ususario
    """
    data = {
        'dataId': instance.dataId,
        'ClienteId': instance.ClienteId,
        'Idade': instance.Idade,
        'EstadoCivil': instance.EstadoCivil,
    }
    ret = dataPredict(data)
    return ret


class Result(models.Model):
    """
    Model com resultado da predicao
    """
    ClienteId = models.CharField(max_length=100)
    Resultado = models.TextField()

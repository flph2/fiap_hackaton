# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from invest import models
from invest import serializers


class PredictViewSet(viewsets.ModelViewSet):
    """
    Metodo de api para receber os
    dados utilizados para sugerir
    os investimentos do usuario
    """
    queryset = models.Predict.objects.all()
    serializer_class = serializers.PredictSerializer


class ResultViewSet(viewsets.ModelViewSet):
    """
    Metodo com resultado das
    predicoes de investimento
    """
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer

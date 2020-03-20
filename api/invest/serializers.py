# encoding: utf-8

from rest_framework import serializers
from invest import models


class PredictSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer do model Predict
    """
    class Meta:
        model = models.Predict
        fields = "__all__"


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = models.Result
        fields = "__all__"

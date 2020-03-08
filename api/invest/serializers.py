# encoding: utf-8

from rest_framework import serializers
from invest import models


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer do model Perfil
    """
    class Meta:
        model = models.Perfil
        fields = "__all__"

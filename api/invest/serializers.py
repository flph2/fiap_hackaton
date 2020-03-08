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


class PagePathSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer do model Perfil
    """
    class Meta:
        model = models.PagePath
        fields = "__all__"


class ProductCatalogSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer do model Perfil
    """
    class Meta:
        model = models.ProductCatalog
        fields = "__all__"



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from invest import models
from invest import serializers


class PerfilViewSet(viewsets.ModelViewSet):
    """
    Metodo de api para exibir todos os
    dados de perfil de usuario existentes
    no dataset 1
    """
    queryset = models.Perfil.objects.all()
    serializer_class = serializers.PerfilSerializer


class PagePathViewSet(viewsets.ModelViewSet):
    """
    Metodo de api para exibir todos os
    dados de perfil de usuario existentes
    no dataset 1
    """
    queryset = models.PagePath.objects.all()
    serializer_class = serializers.PagePathSerializer


class ProductCatalogViewSet(viewsets.ModelViewSet):
    """
    Metodo de api para exibir todos os
    dados de perfil de usuario existentes
    no dataset 1
    """
    queryset = models.ProductCatalog.objects.all()
    serializer_class = serializers.ProductCatalogSerializer

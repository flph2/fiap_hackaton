# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.apps import apps

models = apps.get_models()

for model in models:
    admin.site.register(model)

from __future__ import absolute_import
import pandas as pd
from invest import models
from django.db import transaction


dataset1 = pd.read_csv('../data/Dataset-1.csv', encoding='utf8')
dataset2 = pd.read_csv('../data/Dataset-2.csv', encoding='utf8')
dataset3 = pd.read_csv('../data/Dataset-3.csv', encoding='utf8')

df1 = dataset1.to_dict('records')
df2 = dataset2.to_dict('records')
df3 = dataset3.to_dict('records')

for item in df1:
    try:
        p = models.Perfil(**item)
        p.save()
    except:
        print('ERROR - ',  str(item))
        continue

for item in df2:
    try:
        p = models.PagePath(**item)
        p.save()
    except:
        print('ERROR - ',  str(item))
        continue

for item in df3:
    try:
        p = models.ProductCatalog(**item)
        p.save()
    except:
        print('ERROR - ',  str(item))
        continue


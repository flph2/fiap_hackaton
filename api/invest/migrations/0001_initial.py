# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-08 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClienteId', models.IntegerField()),
                ('Idade', models.IntegerField()),
                ('EstadoCivil', models.CharField(max_length=100)),
                ('BillingCity', models.CharField(max_length=100)),
                ('NivelConhecimentoAtual', models.IntegerField()),
                ('ScoreNivelConhecimento', models.IntegerField()),
                ('PerfilInvestidor', models.IntegerField()),
                ('RendaMensal', models.IntegerField()),
                ('ValorPatrimonio', models.IntegerField()),
                ('Pergunta1', models.CharField(max_length=100)),
                ('Resposta11', models.CharField(max_length=100)),
                ('Pergunta2', models.CharField(max_length=100)),
                ('Resposta21', models.CharField(max_length=100)),
                ('Pergunta3', models.CharField(max_length=100)),
                ('Resposta31', models.CharField(max_length=100)),
                ('Pergunta4', models.CharField(max_length=100)),
                ('Resposta41', models.CharField(max_length=100)),
                ('Pergunta5', models.CharField(max_length=100)),
                ('Resposta51', models.CharField(max_length=100)),
                ('Resposta52', models.CharField(max_length=100)),
                ('Resposta53', models.CharField(max_length=100)),
                ('Resposta54', models.CharField(max_length=100)),
                ('Resposta55', models.CharField(max_length=100)),
                ('Resposta56', models.CharField(max_length=100)),
                ('Resposta57', models.CharField(max_length=100)),
                ('Resposta58', models.CharField(max_length=100)),
                ('Pergunta6', models.CharField(max_length=100)),
                ('Resposta61', models.CharField(max_length=100)),
                ('Resposta62', models.CharField(max_length=100)),
                ('Resposta63', models.CharField(max_length=100)),
                ('Resposta64', models.CharField(max_length=100)),
                ('Resposta65', models.CharField(max_length=100)),
                ('Resposta66', models.CharField(max_length=100)),
                ('Resposta67', models.CharField(max_length=100)),
                ('Resposta68', models.CharField(max_length=100)),
                ('Pergunta7', models.CharField(max_length=100)),
                ('Resposta71', models.CharField(max_length=100)),
                ('Resposta72', models.CharField(max_length=100)),
                ('Resposta73', models.CharField(max_length=100)),
                ('Resposta74', models.CharField(max_length=100)),
                ('Resposta75', models.CharField(max_length=100)),
                ('Pergunta8', models.CharField(max_length=100)),
                ('Resposta81', models.CharField(max_length=100)),
                ('Pergunta9', models.CharField(max_length=100)),
                ('Resposta91', models.CharField(max_length=100)),
                ('ScoreRisco', models.CharField(max_length=100)),
                ('ScoreObjetivos', models.CharField(max_length=100)),
                ('ScoreSituacaoFinanceira', models.CharField(max_length=100)),
                ('Produto', models.CharField(max_length=100)),
                ('NomeDoProduto', models.CharField(max_length=100)),
                ('NomeEmissor', models.CharField(max_length=100)),
                ('TaxaCliente', models.CharField(max_length=100)),
                ('TaxaPreCliente', models.CharField(max_length=100)),
                ('DescricaoProduto', models.CharField(max_length=100)),
                ('ValorMinimoAplicaInicial', models.CharField(max_length=100)),
                ('ValorMinimoAplicacaoAdicional', models.CharField(max_length=100)),
                ('DataVencimento', models.CharField(max_length=100)),
                ('FamiliaCarteira', models.CharField(max_length=100)),
                ('ValorInvestidoAtual', models.CharField(max_length=100)),
                ('ValorRendimento', models.CharField(max_length=100)),
                ('Rentabilidade12Meses', models.CharField(max_length=100)),
                ('RentabilidadeMes', models.CharField(max_length=100)),
                ('RiscoAtivo', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('ProdutoId', models.CharField(max_length=100)),
            ],
        ),
    ]

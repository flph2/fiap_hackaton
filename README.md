# Projeto Hackaton Fiap

## Construindo o ambiente

### Requisitos

```
docker
docker-compose
```

### Executando o ambiente pela primeira vez
dentro do repo git (mesmo diretorio do arquivo docker-compose.yml)
```
docker-compose up -d --build
```

Com isso teremos 2 serviços disponiveis

Spark notebook - http://localhost:8888
Mysql database - localhost:3306

### Acessando pyspark

```
docker logs spark
```
copiar o token e acessar a url http://localhost:8888 e inserir o token na url

Codigo temporario para utilizar pyspark (spark.py dentro do repo git), copiar no jupyter notebook

### Populando os dados
Dentro do notebook (notebooks/felipe_santos.ipynb) existe o passo inicial para fazer ingestão de dados
via pandas para o mysql, basta executar os passos iniciais do notebook para popular a database

```
!pip install sqlalchemy
!pip install pymysql
import pandas as pd 
from sqlalchemy import create_engine

conn = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(user="root",
                               pw="123",
                               host="db",
                               db="invest"))

perfilCliente = pd.read_csv('Dataset-1.csv')
pageViews = pd.read_csv('Dataset-2.csv', )
catProdutos = pd.read_csv('Dataset-3.csv')

catProdutos.to_sql(name='Produtos', con=conn, if_exists = 'replace', index=False)
perfilCliente.to_sql(name='Clientes', con=conn, if_exists = 'replace', index=False)
pageViews.to_sql(name='PageViews', con=conn, if_exists = 'replace', index=False)
```

### Parando o ambiente
Para finalizar os containers digite:
```
docker-compose down
```

### Troubleshooting

Caso a mensagem recebida seja:
```
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' (115)")
```
Provavelmente o container de spark subiu muito rapido e o banco de dados não estava pronto.

Para resolver remova o container de spark e inicie-o novamente
```
docker rm -f spark
docker-compose up -d --build
```

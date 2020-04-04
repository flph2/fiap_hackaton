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

### Descrição do ambiente

3 Containers serão criados

 * api
 * db
 * spark

#### API
Container contendo uma aplicação Django + Django Rest Framework que implementa uma API para integração do modelo, permitindo que utravés de um post com as features de um novo usuário o modelo seja executado e o ID dos produtos recomendados seja exibido:

exemplo:
```
curl -d '{ "userid": 3242, "idade": 32, "perfilInvestidor": 5, "scoreSituacaoFinanceira": 3.0, "scoreNivelConhecimento": 2.0}' -X POST  -H "Content-Type: application/json" 'http://localhost:8000/predict/'
```

```
curl 'http://localhost:8000/result/?userid=2131'
``` 
 
### Acessando pyspark

```
docker logs spark
```
copiar o token e acessar a url http://localhost:8888 e inserir o token na url

Codigo temporario para utilizar pyspark (spark.py dentro do repo git), copiar no jupyter notebook


### Populando os dados
Após o processo de up do ambiente para popular os dados basta executar o comando abaixo.
``
docker exec -ti api python scripts/populate.py`
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

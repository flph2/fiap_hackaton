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

App django - API -  http://localhost:8000

Mysql database - localhost:3306

### Acessando pyspark

```
docker logs spark
```
copiar o token e acessar a url http://localhost:8888 e inserir o token na url

Codigo temporario para utilizar pyspark (spark.py dentro do repo git), copiar no jupyter notebook

### Populando os dados
```
docker exec -ti api scripts/populate.sh
```

### Parando o ambiente
Para finalizar os containers digite:
```
docker-compose down
```

### Troubleshooting
Caso tenha problemas para acessar a app django valide os logs do container
```
docker logs api
```

Caso a mensagem recebida seja:
```
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' (115)")
```
Provavelmente o container de API subiu muito rapido e o banco de dados não estava pronto.

Para resolver remova o container de api e inicie-o novamente
```
docker rm -f api
docker-compose up -d --build
```

# FIAP Hackaton - PI Investimentos

## Membros
Eduardo Siqueira - RM334304 

Felipe Santos - RM333921

Felipe Vieira - RM334147

Paulo Gomes - RM333866

## Descrição do Projeto

A PI Investimentos nos apresentou um problema relacionado a recomendação de produtos para seus clientes, onde sinalizaram a necessidade de um sistema de recomendação para entender o perfil de sesus clientes e sugerir produtos financeiros mais aderentes a suas necessidades.

Alguns pontos (dores) foram sinalizados:

 * Muitas opções de produtos
 * Falta de conhecimento
 * Falta de direcionamento

## Proposta

Após avaliar algumas alternativas, decidimos utilizar um algortimo de recomendação com abordagem híbrida utilizando "conhecimento" colaborativo e baseado em conteudo.

Para isso utilizamos o algoritmo LigthFM fazendo predições baeadas nos dados disponibilizados pela PI.


### Funcionamento da Solução
Para entregar a solução seguimos os seguintes passos

 * EDA com intuito de entender melhor os dados
 * Criação de novos Dataset
   * Normalização e remoção de dados duplicados de Clientes
   * Normalização Relacionamento entre Produto e Cliente
   * Normalização e Relacionamento entre Cliente e Respostas
 * Seleção de Features de Produtos e de Clientes
 * Criação de matrizes esparsas
  * Perfil de Cliente
  * Perfil de Produtos
 * Criação da matriz de interações entre Clientes e Produtos
 * Implementação do modelo de Recomendação Híbrida utilizando LightFM
 * Treinamento dos dados
 * Export do modelo treinado, features e matrizes necessárias para predição
 * Desenvolvimento da API para integração do modelo com as APPs da PI Investimentos
 * Empacotamento em docker para ship em produçao da solução completa.

### Por que utilizar a abordagem Híbrida e o algoritmo lightfm
Após uma série de testes, identificamos que utilizando uma abordagem puramente colaborativa, temos um problema conhecido como "cold start", onde o principal problema é identificar a necessidade do cliente partindo do principio que ele não integragiu com nenhum produto, não fez nenhuma compra ou não demonstrou interesse prévio a algum item do portifólio.

Sendo assim não temos a opção de observar sua preferencia, por isso a abordagem tenta identificar padrões nos perfis de usuario e produtos, baseando-se nessa informaçãode forma a possibilitar uma recomendação mais assertiva e que provavelmente tenha uma maior aderencia a preferencia desse novo usuário

Outra abordagem utilizada é o conceito de "feedback implícito" uma vez que os usuarios que contratam os produtos não os avaliam, mapeando a interação entre o usuario e produto, caracterizada como uma compra.

### Proximos Passos
Abaixo segue uma lista de itens que gostariamos de desenvolver para incrementar a solução como um todo, no entanto demandaria um maior esforço e não foi possivel concluir em tempo hábil.

 * Recomendação de carteira baseada em nivel de risco do produto
  * A idéia principal tem o intuito de categorizar produtos vs perfil de clientes criando uma distribuição de carteira baseada em perfil, onde por exemplo um cliente com perfil de investimento Conservador possui 50% de sua carteira em investimentos de baixo risco, 30% em médio e 20% em alto, e essa distribuição é alterada de acordo com o perfil, o modelo de recomendação hibrida é utilizado para recomendar produtos dentro de um perfil de carteira especifico. Dessa forma a recomendação não é apenas quais produtos comprar e sim uma estratégia de médio/longo prazo para aumento de capital de acordo com o risco de cada perfil.
 * Indentificação de mais features para incrementar o modelo
 * Uma série historica para acompanhar o rendimento de cada produto recomendado, utilizando por exemplo uma estratégia de "Reinforcement Learning"  e reavaliar se aquela recomendação continua fazendo sentido periódicamente, sinalizando ao cliente momentos em que é interessante sair de um investimento que possui e investir em um novo.
 * Utilizar PageViews pra incrementar o modelo, utilizando a visão de paginas mais visitadas como input para o processo de feedback implícito

### Entrega do trabalho
A elaboração do modelo utilizando LightFM e seu resultado estão disponiveis no [notebook](notebooks/lightfm3.ipynb)

### Ambiente
O processo para iniciar um novo ambiente ou utilizar para ambiente de desenvolvimento, criando a infra necessária está disponivel aqui [link](doc/DEVELOP.md)

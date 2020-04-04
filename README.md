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


### Documentação de desenvolvimento
Para iniciar um novo ambiente e desenvolvimento, criando a infra necessária utilize [link]('doc/DEVELOP.md')
/

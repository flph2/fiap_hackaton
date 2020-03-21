#!/usr/bin/python
from sqlalchemy import create_engine
import pandas as pd
conn = create_engine(
    "mysql+pymysql://{user}:{pw}@{host}/{db}"
    .format(user="root",
    pw="123",
    host="db",
    db="invest")
)

print("Connectado ao banco")

perfilCliente = pd.read_csv('/root/data/Dataset-1.csv')
perfilClientev2 = pd.read_csv('/root/data/Dataset-1-v2.csv')
pageViews = pd.read_csv('/root/data/Dataset-2.csv', )
catProdutos = pd.read_csv('/root/data/Dataset-3.csv')
print("Pandas data Load")

catProdutos.to_sql(name='Produtos', con=conn, if_exists = 'replace', index=False)
print('Produtos inserido no DB')
perfilCliente.to_sql(name='Clientes', con=conn, if_exists = 'replace', index=False)
print('Clientes inserido no DB')
perfilClientev2.to_sql(name='Clientesv2', con=conn, if_exists = 'replace', index=False)
print('Clientesv2 inserido no DB')
pageViews.to_sql(name='PageViews', con=conn, if_exists = 'replace', index=False)
print('PageViews inserido no DB')

#  Cli_Clientes
q = '''
CREATE TABLE `cli_Clientes`
( 
  `userid`                                      int     NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `userid_aux`                          text    DEFAULT NULL,
  `idade`                                       double  DEFAULT NULL,
  `genero`                                      text,
  `estadocivil`                         text,
  `billingcity`                         text,
  `profissaopessoa`             text,
  `patrimonioautomoveis`        double DEFAULT NULL,
  `patrimonioimoveis`           double DEFAULT NULL,
  `patrimonioinvestimentos` double DEFAULT NULL,
  `patrimoniooutros`            double DEFAULT NULL,
  `nivelconhecimentoatual`      double DEFAULT NULL,
  `scorenivelconhecimento`      double DEFAULT NULL,
  `perfilinvestidor`            bigint(20) DEFAULT NULL,
  `rendamensal`                         double DEFAULT NULL,
  `valorpatrimonio`             double DEFAULT NULL,
  `scorerisco`                          double DEFAULT NULL,
  `scoreobjetivos`                      double DEFAULT NULL,
  `scoresituacaofinanceira` double DEFAULT NULL,
  `createddate`                         text,
  `dataclienteefetivado`        text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
'''
conn.execute(q)

print('tabela cli_clientes criada')

q = '''
insert into cli_Clientes
(       userid_aux,idade,genero,estadocivil,billingcity,profissaopessoa,patrimonioautomoveis,patrimonioimoveis,patrimonioinvestimentos,
        patrimoniooutros,nivelconhecimentoatual,scorenivelconhecimento,perfilinvestidor,rendamensal,valorpatrimonio,
        scorerisco,scoreobjetivos,scoresituacaofinanceira,createddate,dataclienteefetivado
)
SELECT
DISTINCT
        userid,
        idade,
        genero,
        estadocivil,
        billingcity,
        profissaopessoa,
        patrimonioautomoveis,
        patrimonioimoveis,
        patrimonioinvestimentos,
        patrimoniooutros,
        nivelconhecimentoatual,
        scorenivelconhecimento,
        perfilinvestidor,
        rendamensal,
        valorpatrimonio,
        scorerisco,
        scoreobjetivos,
        scoresituacaofinanceira,
        createddate,
        dataclienteefetivado
from Clientesv2;
'''

conn.execute(q)
print('Cli_clientes data load')
# Fim Cli_Clientes

# Inicio cli_Respostas
q = '''
CREATE TABLE `cli_Respostas`
(
  `userid`                                      int     NOT NULL ,
  `Respostas1`                          text    DEFAULT NULL,
  `Respostas2`                          text    DEFAULT NULL,
  `Respostas3`                          text    DEFAULT NULL,
  `Respostas4`                          text    DEFAULT NULL,
  `Respostas51`                         text    DEFAULT NULL,
  `Respostas52`                         text    DEFAULT NULL,
  `Respostas53`                         text    DEFAULT NULL,
  `Respostas54`                         text    DEFAULT NULL,
  `Respostas55`                         text    DEFAULT NULL,
  `Respostas56`                         text    DEFAULT NULL,
  `Respostas57`                         text    DEFAULT NULL,
  `Respostas58`                         text    DEFAULT NULL,
  `Respostas61`                         text    DEFAULT NULL,
  `Respostas62`                         text    DEFAULT NULL,
  `Respostas63`                         text    DEFAULT NULL,
  `Respostas64`                         text    DEFAULT NULL,
  `Respostas65`                         text    DEFAULT NULL,
  `Respostas66`                         text    DEFAULT NULL,
  `Respostas67`                         text    DEFAULT NULL,
  `Respostas68`                         text    DEFAULT NULL,
  `Respostas71`                         text    DEFAULT NULL,
  `Respostas72`                         text    DEFAULT NULL,
  `Respostas73`                         text    DEFAULT NULL,
  `Respostas74`                         text    DEFAULT NULL,
  `Respostas75`                         text    DEFAULT NULL,
  `Respostas8`                          text    DEFAULT NULL,
  `Respostas9`                          text    DEFAULT NULL
);
'''
conn.execute(q)

print('tabela cli_Respostas criada')
q = '''
INSERT INTO cli_Respostas (userid,Respostas1,Respostas2,Respostas3,Respostas4,Respostas51,Respostas52,Respostas53,Respostas54,Respostas55,
                                                        Respostas56,Respostas57,Respostas58,Respostas61,Respostas62,Respostas63,Respostas64,Respostas65,Respostas66,Respostas67,
                                                        Respostas68,Respostas71,Respostas72,Respostas73,Respostas74,Respostas75,Respostas8,Respostas9
)
select
distinct
        c.userid,
        REPLACE(COALESCE(resposta11,''),'None',''),
        REPLACE(COALESCE(resposta21,''),'None',''),
        REPLACE(COALESCE(resposta31,''),'None',''),
        REPLACE(COALESCE(resposta41,''),'None',''),
        REPLACE(COALESCE(resposta51,''),'None',''),
        REPLACE(COALESCE(resposta52,''),'None',''),
        REPLACE(COALESCE(resposta53,''),'None',''),
        REPLACE(COALESCE(resposta54,''),'None',''),
        REPLACE(COALESCE(resposta55,''),'None',''),
        REPLACE(COALESCE(resposta56,''),'None',''),
        REPLACE(COALESCE(resposta57,''),'None',''),
        REPLACE(COALESCE(resposta58,''),'None',''),
        REPLACE(COALESCE(resposta61,''),'None',''),
        REPLACE(COALESCE(resposta62,''),'None',''),
        REPLACE(COALESCE(resposta63,''),'None',''),
        REPLACE(COALESCE(resposta64,''),'None',''),
        REPLACE(COALESCE(resposta65,''),'None',''),
        REPLACE(COALESCE(resposta66,''),'None',''),
        REPLACE(COALESCE(resposta67,''),'None',''),
        REPLACE(COALESCE(resposta68,''),'None',''),
        REPLACE(COALESCE(resposta71,''),'None',''),
        REPLACE(COALESCE(resposta72,''),'None',''),
        REPLACE(COALESCE(resposta73,''),'None',''),
        REPLACE(COALESCE(resposta74,''),'None',''),
        REPLACE(COALESCE(resposta75,''),'None',''),
        REPLACE(COALESCE(resposta81,''),'None',''),
        REPLACE(COALESCE(resposta91,''),'None','')
from invest.Clientesv2 v2
inner join cli_Clientes c
                on v2.userid = c.userid_aux

'''

conn.execute(q)
print('cli_respostas data load')
# Fim Respostas

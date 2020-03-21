

CREATE TABLE cli_Produtos
(
	`userid`	 		int,
	`produtoid`  		int,
	`valorrendimento`	double,
	`dataefetivacao`    text
);

INSERT INTO cli_Produtos (USERID, PRODUTOID, VALORRENDIMENTO, DATAEFETIVACAO)
SELECT
DISTINCT
	c.userid,
	P.dataId as produtoid,
	v2.valorrendimento,
	v2.dataefetivacao
from Clientesv2 v2

inner join cli_Clientes c 
		on v2.userid = c.userid_aux

inner join Produtos P		
		on P.ProdutoId = v2.produto

UNION ALL
select 
	distinct
	0,
	p.dataid,
	0,
	''
from Produtos p
where not exists (select 1 from Clientesv2 v2 where v2.produto = p.ProdutoId)
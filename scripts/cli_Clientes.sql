CREATE TABLE `cli_Clientes` 
(
  `userid` 					int 	NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `userid_aux`				text    DEFAULT NULL,
  `idade` 					double 	DEFAULT NULL,
  `genero` 					text,
  `estadocivil` 			text,
  `billingcity` 			text,
  `profissaopessoa` 		text,
  `patrimonioautomoveis` 	double DEFAULT NULL,
  `patrimonioimoveis` 		double DEFAULT NULL,
  `patrimonioinvestimentos` double DEFAULT NULL,
  `patrimoniooutros` 		double DEFAULT NULL,  
  `nivelconhecimentoatual` 	double DEFAULT NULL,
  `scorenivelconhecimento` 	double DEFAULT NULL,
  `perfilinvestidor` 		bigint(20) DEFAULT NULL,
  `rendamensal` 			double DEFAULT NULL,
  `valorpatrimonio` 		double DEFAULT NULL,  
  `scorerisco` 				double DEFAULT NULL,
  `scoreobjetivos` 			double DEFAULT NULL,
  `scoresituacaofinanceira` double DEFAULT NULL,
  `createddate` 			text,
  `dataclienteefetivado` 	text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


insert into cli_Clientes 
(	userid_aux,idade,genero,estadocivil,billingcity,profissaopessoa,patrimonioautomoveis,patrimonioimoveis,patrimonioinvestimentos,
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

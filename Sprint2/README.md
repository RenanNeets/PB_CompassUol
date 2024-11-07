# Sprint 2
### Informações
Nessa sprint o foco maior foi em aprender SQL e realizar os Modelo Relacional e Dimencional, além de ter o primeiro contato com cursos da AWS e a lista de exercícios. No estudo de SQL não se teve muita dificuldade de estudar e no curso da AWS o único problema foi em acessar o curso, caso que foi solucionado de forma rápida pela Scrum Maste Marli. Mas também, para resolver os exercícios e o desafio não se teve muita dúvida ou incerteza, somente certos momentos que tive dificuldade com a lógica para resolver um exercício ou uma parte do

### Certificados
Nesta sprint além do curso proporcinado pela Udemy, também tive um primeiro contato com o curso AWS, o que possibilitou de adquirir o certificado do curso *Sales Accreditation* e o seu distintivo.

- [AWS Skill Builder - AWS Partner: Sales Accreditation](./certificados/AWS_Partner_Sales_Accresditation.pdf)

### Desafio
O desafio foi dividido em duas etapas: a criação do modelo relacional e a construção do modelo dimensional. Na primeira etapa, o ponto de partida foi uma tabela única com todos os atributos e dados do banco, a qual foi utilizada para distribuir os dados em tabelas normalizadas. Primeiramente, foi criada a tabela de clientes, com chave primária e atributos próprios, seguida das tabelas de combustível, carro e vendedor, cada uma organizada com suas respectivas chaves e dados importados da tabela original. Após estruturar as tabelas menores, criei a tabela de locação com as devidas relações com outras tabelas. Finalizada a modelagem relacional, a tabela original foi excluída, pois os dados já estavam organizados. 

Na segunda etapa, desenvolvi o modelo dimensional com tabelas de dimensão e fato, interligando-as para análise de dados. A função view foi sugerida para criar o modelo dimensional, mas, devido às limitações de relacionamento, optei por construir o modelo diretamente com tabelas.
### Evidências
Os modelos e a parte do código usado para criar os modelos já fazendo a normalização dos dados, tudo isso para que as imagens usadas no *readme* do diretório *desafio*.

### Exercícios
Nesta sprint a realização dos desafios foi tranquila e rápida na sua maioria, contando com certos exercícios que me fizeram demorar mais tempo para resolver, mas nenhum que não fosse possível solucionar.

Nesta pasta a organização se basea em duas partes, uma que se encontra os exercícios da linguagem SQL para caso de estudo, envolvendo os bancos de dados *biblioteca* e *loja* ambos oferecidos para resolver o exercícios, e outro que se encontra os exercícios que envolve exerportação dos dados. Nesta segunda parte foi usado de novo o banco de dados *biblioteca* para fazer a exportação das querrys, mas no formato .csv e com separador específico para cada exercício.
- [Exercício de Caso de Estudo](./exercicios/casoEstudo/)
- [Exercício Exportação de Dados](./exercicios/exportacaoDados/)

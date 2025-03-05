# Sprint 9
### Informações
Nessa sprint foi focada inteiramente para resolver o desafio, sem incluir cursos da Udemy ou da AWS. Mas aproveitei para além de realizar o desafio realizar os cursos opcionais da trilha e estudar para a prova *AWS Certified Cloud Practitioner CLF-C02 2025*. O desafio se baseou em realizar as perguntas para serem respondidas depois, criar o modelo dimencional das tabelas em forma de código e também a forma visual dele, tudo sendo realizado sem muita dificuldade.

### Certificados
Nesta sprint o foco foi em cursos proporcionados pela Udemy, sem ter envolvimento com a AWS. Isso fez com que a pasta certificados fique vázia nessa sprint.
### Desafio
O desafio dessa sprint dá continuidade ao *Desafio Filmes e Séries*, focado na construção de um Data Lake com etapas de ingestão, armazenamento, processamento e consumo. A análise dos dados incluiu os arquivos CSV e uso da API TMDB. Que foram formuladas perguntas sobre o sucesso e evolução dessas produções, bem como sobre seus atores. Na modelagem de dados da camada *Refined*, nova camada a ser gerada nesse desafio, utilizou-se o DBeaver para criar dimensões como atores, data, gênero, países de produção, produtora e descricção além da tabela fato séries. O pocessamento foi realizado no AWS Glue, configurando permissões IAM e criando um banco de dados no AWS Lake Formation. O job do Glue foi desenvolvido em Spark para processar os arquivos Parquet da camada *Trusted*, gerando dimensões e fato. Após a execução e correção de erros, os arquivos foram armazenados no bucket S3 e convertidos em tabelas usando o AWS Glue Crawler. As tabelas foram validadas no AWS Athena, confirmando a extração correta das informações.

### Evidências
O resultado que obitive realizando o desafio, sendo criando os sripts necessários e os resultados das ações dele. Tudo em forma de imagenm para ser usado no *readme* do diretório *desafio*.

### Exercícios
Nesta sprint não se teve lista de exercícios para ser realizada, isso proporcionou um foco direto em resolver o desafio solicitado

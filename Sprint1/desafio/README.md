# Desafio

### Passo a passo
Para rodar o código *processamento_de_vendas.sh*, siga a seguinte ordem:
- Prepare a pasta _ecommerce_ com o arquivo *dados_de_vendas.csv* e os dois arquivos com extensão .sh dentro.
- Em seguida, rode o arquivo *processamento_de_vendas.sh* com o comando *bash processamento_de_vendas.sh* no terminal da pasta *ecommerce*.

Seguindo estes passos, atenderá aos preparativos propostos na apresentação do desafio e poderá efetuar o funcionamento do programa, gerar as pastas solicitadas, além de transferir, renomear e compactar o arquivo *dados_de_vendas.csv* e obter um relatório com as características necessárias.

_foto dos preparativos do desafio_

Para rodar o código *consolidador_de_processamento_de_vendas.sh*, será necessário executar o código *processamento_de_vendas.sh* mais de uma vez. Depois de rodar o arquivo *processamento_de_vendas.sh* e gerar dois relatórios e dois arquivos de backup, siga as instruções:
- Rode o arquivo *consolidador_de_processamento_de_vendas.sh* com o comando *bash consolidador_de_processamento_de_vendas.sh* no terminal da pasta *ecommerce*.

Após a execução do programa, ele entregará um relatório final com a junção dos relatórios gerados pelo arquivo *processamento_de_vendas.sh*.

### Início
Comecei a realizar o desafio lendo a proposta e tentando dividi-lo em partes para resolvê-lo aos poucos. Em alguns momentos, surgiram dúvidas sobre como executar certos pontos do desafio, mas consegui resolvê-las consultando minha monitora e colegas da turma, e tentando resolver cada etapa isoladamente, sem a necessidade de alterar partes anteriores do código.

### Meio
Na metade do desafio, enfrentei o problema de programar o funcionamento do programa com um agendamento específico. A dificuldade era configurar o _crontab -e_ para rodar em um horário determinado. Apesar de programá-lo, ele executou com um atraso de menos de 15 segundos. Todos os resultados foram entregues no mesmo minuto e segundo, com uma diferença exata de 1 segundo entre alguns arquivos, ficando, em média, com 46 segundos de execução.

_foto do crontab e dos resultados_

Outro problema encontrado durante a execução foi a contagem de itens únicos da lista de produtos vendidos. Nos primeiros três dias, segui uma lógica diferente da aplicada no último dia. Esta mudança na lógica ocorreu após os relatos de colegas sobre os resultados de seus programas e uma revisão de última hora no meu código. O problema na contagem de itens únicos foi causado por uma seleção incorreta na hora de contar: nos primeiros dias, contei pela categoria "produto", mas o correto seria contar pelo "id" para contabilizar corretamente a quantidade de produtos vendidos.

_foto do código na íntegra_

### Final
No momento final do desafio e ao término dos 4 dias seguidos de execução, o programa estava em perfeito estado, rodando o último dia e criando o arquivo da forma correta, sem problemas e gerando o resultado esperado.

_foto do último relatório feito_

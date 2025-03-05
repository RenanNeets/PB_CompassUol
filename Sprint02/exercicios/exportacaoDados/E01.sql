SELECT
livro.cod AS CodLivro,
livro.titulo AS Titulo,
autor.codautor AS CodAutor,
autor.nome AS NomeAutor,
livro.valor AS Valor,
editora.codeditora AS CodEditora,
editora.nome AS NomeEditora
FROM livro
FULL JOIN autor ON livro.autor = autor.codautor
FULL JOIN editora ON livro.editora = editora.codeditora
ORDER BY livro.valor DESC
LIMIT 10
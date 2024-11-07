SELECT
editora.codeditora AS CodEditora,
editora.nome AS NomeEditora,
COUNT(livro.cod) AS QuantidadeLivros
FROM editora
FULL JOIN livro ON editora.codeditora = livro.editora
GROUP BY CodEditora, NomeEditora
ORDER BY QuantidadeLivros DESC
LIMIT 5
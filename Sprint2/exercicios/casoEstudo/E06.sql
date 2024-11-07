SELECT autor.codautor, autor.nome, COUNT(livro.autor) AS quantidade_publicacoes
FROM livro
JOIN autor ON autor.codautor = livro.autor
GROUP BY livro.autor
ORDER BY quantidade_publicacoes DESC
LIMIT 1

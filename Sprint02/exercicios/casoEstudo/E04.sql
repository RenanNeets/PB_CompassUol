SELECT autor.nome, autor.codautor, autor.nascimento, COUNT(livro.cod) AS quantidade
FROM autor
LEFT JOIN livro ON livro.autor = autor.codautor
GROUP BY autor.nome, autor.codautor, autor.nascimento
ORDER BY autor.nome

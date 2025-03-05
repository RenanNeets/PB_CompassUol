SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON livro.autor = autor.codautor
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY autor.nome ASC
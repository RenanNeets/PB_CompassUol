SELEcT COUNT(livro.cod) AS quantidade, nome, endereco.estado, endereco.cidade
FROM editora
JOIN livro ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC
LIMIT 5
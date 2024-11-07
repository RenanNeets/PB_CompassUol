SELECT autor.nome
FROM autor
FULL JOIN livro ON autor.codautor = livro.autor
WHERE livro.autor IS NULL
ORDER BY livro.autor
SELECT tbestoqueproduto.cdpro, tbvendedor.cdvdd
FROM tbvendas
JOIN tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE DATE(tbvendas.dtven)> '2014-02-03' AND DATE(tbvendas.dtven) < '2018-02-02' AND tbvendas.status = 'Concluído'
GROUP BY tbestoqueproduto.cdpro, tbvendas.nmpro
ORDER BY COUNT(tbvendas.cdvdd) DESC
LIMIT 1

SELECT tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc,
ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS valor_total_vendas
FROM tbdependente
JOIN tbvendedor ON tbdependente.cdvdd = tbvendedor.cdvdd
JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbdependente.cddep, tbdependente.nmdep
ORDER BY valor_total_vendas
LIMIT 1

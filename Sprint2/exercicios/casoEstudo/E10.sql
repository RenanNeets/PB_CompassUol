SELECT tbvendedor.nmvdd AS vendedor,
ROUND(SUM(tbvendas.qtd * tbvendas.vrunt),2) AS valor_total_vendas,
ROUND((SUM((tbvendas.qtd * tbvendas.vrunt)* tbvendedor.perccomissao))/100, 2) AS comissao
FROM tbvendedor
FULL JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.perccomissao
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd, tbvendedor.perccomissao
ORDER BY comissao DESC

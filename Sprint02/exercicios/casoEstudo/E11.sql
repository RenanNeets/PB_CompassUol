SELECT tbvendas.cdcli, tbvendas.nmcli, SUM(tbvendas.qtd * tbvendas.vrunt) AS gasto
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.cdcli, tbvendas.nmcli
ORDER BY gasto DESC
LIMIT 1
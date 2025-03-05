if [ ! -d 'vendas' ]; then
	mkdir vendas
fi
cp dados_de_vendas.csv vendas/
cd vendas
data=$(date "+%Y%m%d")
mv dados_de_vendas.csv dados-$data.csv
if [ ! -d 'backup' ]; then
	mkdir backup
fi
cp dados-$data.csv backup
cd backup/
mv *.csv backup-dados-$data.csv
touch relatorio-$data.txt
date "+%Y/%m/%d %H:%M" > relatorio-$data.txt
awk -F',' 'NR==2 {print $5}' *.csv >> relatorio-$data.txt
awk -F',' 'END {print $5}' *.csv >> relatorio-$data.txt
awk -F',' ' {print $1}' *.csv | sort | uniq | wc -l>> relatorio-$data.txt
head -n 11 *.csv >> relatorio-$data.txt
zip backup-dados-$data.zip *.csv
rm *.csv
cd ..
rm *.csv

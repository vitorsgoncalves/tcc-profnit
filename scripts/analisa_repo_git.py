
# Este script analisa os repositórios git contidos no diretório em que é executado
# em seguida, retorna arquivos CSV contendo a quantidade de commits por mês, autores/quantidade de commits por autor e novos autores por mês
# os resultados são gravados no próprio diretório de execução
# OBS: É necessário obter um binário do software mergestat para a execução deste script
# O mergestat pode ser obtido por meio do link: https://github.com/mergestat/mergestat-lite

import os, subprocess
import csv
import sqlite3
from os import path


pasta = os.path.abspath(os.getcwd())

total_commits = 0 
autores = []
commits_mes = []
autores_mes = []
meses_repetidos = {}
qt_repetida = []

def minerar(dirs):
	
	
	global total_commits 
	global autores
	global commits_mes
	global autores_mes
	global meses_repetidos
	global qt_repetida
	
	
	#obtém o total de commits
	query = subprocess.check_output(['mergestat', 'select count(*) from commits', "--repo="+ dirs, "-f", "single"])
	total_commits += int(query)
	
	#obtém uma lista de autores e commits por autor
	query = subprocess.check_output(['mergestat', 'select author_name, strftime(\'%Y-%m\',min(author_when)) as data ,count(author_name) as author_commits from commits  group by author_name ', "--repo="+ dirs, "-f", "json"]) 

	tempdict = {}
	exec( "temp = " + query.decode('utf-8').replace("null", "'null'") , tempdict)
	temp = tempdict['temp']
	for dicio in temp:
		achou = False
		for dicio2 in autores:
			if dicio2["author_name"] == dicio["author_name"]:
				dicio2["author_commits"] += dicio["author_commits"]
				achou = True
				if dicio["data"] in meses_repetidos:
					meses_repetidos[dicio["data"]] += 1 	
				else:
					meses_repetidos[dicio["data"]] = 1 
				break
		if not achou:
			autores.append(dicio)
			

	# obtém os commits por mês
	query = subprocess.check_output(['mergestat', 'select strftime(\'%Y-%m\', author_when) as data, count(author_when) as commits from commits group by data ', "--repo="+ dirs, "-f", "json"]) 	

	exec( "temp = " + query.decode('utf-8').replace("null", "'null'"), tempdict )
	temp = tempdict['temp']

	for dicio in temp:
		achou = False
		for dicio2 in commits_mes:
			if dicio2["data"] == dicio["data"]:
				dicio2["commits"] += dicio["commits"]
				achou = True
				break
		if not achou:
			commits_mes.append(dicio)
	
	
	#obtém os autores por mes
	query = subprocess.check_output(['mergestat', 'select count(author_name) as autores, strftime(\'%Y-%m\', data2) as data from (select distinct author_name, min(author_when) as data2 from commits group by author_name )  group by data', "--repo="+ dirs, "-f", "json"]) 
	exec( "temp = " + query.decode('utf-8').replace("null", "'null'") , tempdict)
	temp = tempdict['temp']
		
	for dicio in temp:
		achou = False
		for dicio2 in autores_mes:
			if dicio2["data"] == dicio["data"]:
				dicio2["autores"] += dicio["autores"]
				achou = True
				break
		if not achou:
			autores_mes.append(dicio)
		


for dirs in next(os.walk(pasta))[1]:
	print(dirs)
	
	if path.exists(dirs + "/.git") and dirs != "external":
		minerar(dirs)
	else:
		
		for subdirs in next(os.walk(dirs))[1]:
			if path.exists(dirs + "/.git"):
				minerar(dirs)		
	
# remove os autores duplicados
for mes in autores_mes:
	if mes["data"] in meses_repetidos:
		mes["autores"] -= meses_repetidos[mes["data"]]



with open('totais.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['autores', 'commits'])
    writer.writerow([str(len(autores)), str(total_commits)])

with open('commits_mes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['data','commits'])
    writer.writeheader()
    writer.writerows(commits_mes)

with open('autores_mes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['data','autores'])
    writer.writeheader()
    writer.writerows(autores_mes)
    
with open('autores.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['author_name','author_commits', 'data'])
    writer.writeheader()
    writer.writerows(autores)    
    

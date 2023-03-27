import csv
import datetime
import os
import re
import sys

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

caminho_entrada = sys.argv[1]
caminho_saida = sys.argv[2]
palavras = sys.argv[3:]

historico = []

for files in os.listdir(caminho_entrada):
    if files.endswith(".csv"):
        ano = files[3:10]
        
        caminho = open(caminho_entrada + "/" + files, "r")
        arquivo = csv.DictReader(caminho)
        
        nbom = 0
        nruim = 0
        nneutro = 0
        soma_sentimento = 0
        
        with open(caminho_saida + "/" + files[:-4] +'_setimento.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, arquivo.fieldnames + ["vader"])
            writer.writeheader()
            
            for row in arquivo:
                
                tex_original = row['texto']
                
                a = tex_original.split('\n')
                b = []
                
                for trecho in a:
                    if any(palavra in trecho.lower() for palavra in palavras):
                        b += [trecho]
                
                if len(''.join(a).strip('\n').strip(' ')) == 0:
                    continue
                else:
                    tex = '\n'.join(b)
                
                    data = datetime.datetime.fromtimestamp(int(row['data'])) 

                    ss = sia.polarity_scores(tex)
                    valor_vader = ss["compound"]
                    
                    row.update({"vader": valor_vader})

                    #print(valor_vader)
                    if valor_vader > 0.05:
                        nbom += 1

                    elif valor_vader < -0.05:
                        nruim += 1
    
                    else:
                        nneutro += 1


                    soma_sentimento += valor_vader
                    
                    writer.writerow(row)

        media = soma_sentimento / (nneutro+nruim+nbom) if (nneutro+nruim+nbom) else 0
        historico.append({'ano': ano, 'nbom': nbom, 'nneutro': nneutro, 'nruim': nruim , 'media': media})
        print(historico)

    
with open(caminho_saida + '/sentimento_mes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['ano','nbom', 'nneutro', 'nruim', 'media' ])
    writer.writeheader()
    writer.writerows(historico)


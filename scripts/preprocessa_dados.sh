#!/bin/bash

#Este script preprocessa os dados obtidos a partir do PushShift, extraindo apenas as linhas que contenham as palavras-chave desejadas e gerando arquivos no formato CSV

#Para isso, devem ser passados, como parâmetro a palavra-chave desejada, o caminho onde s encontram os arquivos compactados, o caminho de saída para os CSV gerados, e, opcionalmente, um caminho temporário para realizar o processamento. 

# Utilização: ./preprocessa_dados.sh <palavra-chave> <diretório de origem dos dados> <diretório de saída para os arquivos CSV <diretório temporário opcional>>

#Se forem utilizadas mais de uma palavra-chave como entrada, utilize o formato "palavra1.*palavra2|palavra2.*palavra1", enviando o argumento entre aspas.

# Verifica se foram fornecidos os argumentos necessários
if [ $# -lt 3 ] || [ $# -gt 4 ]; then
  echo -e "Erro: argumentos inválidos.\n"
  echo -e  "Utilização: ./preprocessa_dados.sh <palavra-chave> <diretório de origem dos dados> <diretório de saída para os arquivos CSV> <diretório temporário opcional> \n\nPara maiores informações, consultar a ajuda fornecida no cabeçalho deste script \n"
  exit 1
fi

palavra_chave="$1"
caminho_entrada="$2"
caminho_saida="$3"
caminho_processamento="${4:-$caminho_entrada}"

for caminho_arquivo in "$caminho_entrada"/*.zst; do
    arquivo="$(basename "$caminho_arquivo" .zst)"
    
    if [ "$caminho_processamento" != "$caminho_entrada" ]; then
        cp "$caminho_arquivo" "$caminho_processamento/$arquivo.zst"
        caminho_arquivo="$caminho_processamento/$arquivo.zst"
    fi

    echo '"texto","sub","data","autor","id"' > "$caminho_saida/$arquivo.csv"

    zstd -dcf --long=31 "$caminho_arquivo" | grep -i -E $palavra_chave | \
    jq -r '[.body, .subreddit, .created_utc, .author, .id] | @csv' >> "$caminho_saida/$arquivo.csv"
    
    if [ "$caminho_processamento" != "$caminho_entrada" ]; then
        rm "$caminho_processamento/$arquivo.zst"
    fi
done


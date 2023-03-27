# Analisador de sentimento

Este software foi criado como produto da dissertação de mestrado de título "Fatores influenciadores do sucesso em projetos de software livre: um estudo de caso da descontinuação do Firefox OS" e entregue como produto tecnológico para o programa de mestrado PROFNIT. Sua idealização se deu a partir dos procedimentos metodológicos realizados no estudo, como uma forma de facilitar a realização de análises de sentimento por novos pesquisadores, principalmente de áreas de eestudo não tecnológicas, de forma a reduzir as barreiras de facilitar a viabilidade de novos estudos.

Trata-se de uma ferramenta simplificada para realização de análise de sentimento a partir da metodologia [VADER](https://github.com/cjhutto/vaderSentiment) para analisar a intensidade de sentimento de grandes quantidades de texto. Esta ferramenta foi projetada para uso em aplicações científicas, quando a análise de sentimento pode ser útil para avaliar a opinião dos participantes em um estudo ou para analisar comentários de usuários em fóruns ou redes sociais. 

## Funcionalidades

- Importação de dados no formato CSV: O software permite a leitura de dados no formato CSV, devido à sua praticidade e popularidade em aplicações científicas. O usuário pode optar entre importar um único arquivo CSV ou vários arquivos CSV para análise.
- Exportação de dados no formato CSV: O software exporta os dados analisados em um novo arquivo CSV, sem modificar o arquivo de origem, contendo a estrutura do arquivo original, adicionada de uma nova coluna, com o valor agregado de intendidade de sentimento calculada. É também exportado um arquivo CSV auxiliar, contendo uma linha para cada CSV de entrada e a intensidade média dos textos de cada um deles, para facilitar a obtenção de médias nos casos em que os dados são organizados em múltiplos CSVs separados por períodos de tempo 
- Seleção da coluna a ser analisada: O usuário pode escolher qual coluna do CSV será analisada, de forma que o software analisará apenas o texto contido na coluna selecionada, ignorando as demais.
- Filtragem por palavras-chave: O usuário pode escolher uma ou mais palavras-chave para filtrar os dados. Apenas as linhas que contêm pelo menos uma das palavras-chave selecionadas serão analisadas. Esta funcionalidade permite auxiliar a análise de dados com pouco ou nenhum pré-processamento.

## Utilização

### Instalação

Se você utiliza sistemas operacionais Windows ou Linux em arquitetura X64, foram criados executáveis que podem ser baixados e executados diretamente, a partir do link abaixo, sem a necessidade de conhecimentos técnicos específicos:

(link a ser definido)

Caso utilize um sistema diferente, ou o procedimento acima não funcione, siga as instruções abaixo:

1. Instale o Python em sua máquina, se não estiver disponível, a partir das instruções do site oficial:

	[Página de instruções de instalação do Python](https://www.python.org/about/gettingstarted/)

1. Baixe ou clone o repositório do software a partir do comando:  

	` git clone (colocar url)` 

2. Entre no diretório do software:

	` cd (colocar caminho)` 

3. Instale os pacotes Python necessários usando o comando 

	`pip install -r requirements.txt`

4. Execute o software a partir do comando abaixo:

	`python (nome final)`

### Execução

Ao iniciar o software, será exibida uma tela como essa:

![Tela principal do software, exibindo as opções disponívels](https://github.com/vitorsgoncalves/tcc-profnit/blob/main/produto/imagens/tela%20principal.png?raw=true "Tela principal do software")

A tela principal consiste de dois campos de seleção de diretório, dois campos para inserção de parâmetros textuais, e os botões para iniciar e cancelar o processo.

No campo de "Entrada", deve ser definido o diretório no qual se encontram os arquivos CSV a resem analisados. É importante destacar que todos os CSVs dentro desse diretório serão lidos, e que estes devem conter campos padronizados. Recomenda-se que este diretório contenha apenas os arquivos desejados para o estudo.

No campo de "Saída", deve ser definido o caminho para gravação dos arquivos CSV gerados pelo software. Recomenda-se que não seja o mesmo diretório de entrada, para evitar que estes sejam lidos como entrada ao se executar novamente o procedimento.

O campo "Nome da coluna" deve ser preenchido com o nome da coluna do arquivo CSV que contenha os dados textuais a serem analisados. 

Já o campo "Palavras-chave" é opcional, e deve ser preenchido com as palavras-chave desejadas nos casos em que nem todas as linhas do arquivo CSV deverão ser analisadas. Ao se utilizar esse recurso, serão consideradas apenas as lihas que contenham pelo menos uma das palavras-chave inseridas e o arquivo de saída conterá apenas as linhas classificadas.

Um exemplo de preenchimento dos campos pode ser visto na figura abaixo:

![Imagem da tela principal com os dados preenchidos](https://github.com/vitorsgoncalves/tcc-profnit/blob/main/produto/imagens/dados%20inseridos.png?raw=true "Imagem da tela principal com os dados preenchidos")

Após preencher os dados, pressione o botão "Iniciar e aguarde a execução em uma nova tela. Dependendo do tamanho dos arquivos de entrada, o processo pode levar muito tempo. Após o término, será exibido um diálogo indicando o fim da operação.

Os resultados podem ser encontrados na pasta definida como saída. O arquivo gerado é uma cópia do arquivo original, com uma nova coluna referente ao valor calculado como intensidade de sentimento. Um exemplo de arquivos gerados pode ser visto na simagens abaixo:

Exemplo de saída de dados:

![Imagem demonstrando um exemplo de saída de dados](https://github.com/vitorsgoncalves/tcc-profnit/blob/main/produto/imagens/resultado.png?raw=true "Exemplo de arquivo de saída")

Exemplo do segundo arquivo de saída, com os números de comentários de cada tipo e as médias calculadas para cada arquivo de entrada:

![Exemplo do segundo arquivo de saída, com os números de comentários de cada tipo e as médias calculadas para cada arquivo de entrada](https://github.com/vitorsgoncalves/tcc-profnit/blob/main/produto/imagens/resultado2.png?raw=true "Exemplo do segundo arquivo de saída, com os números de comentários de cada tipo e as médias calculadas para cada arquivo de entrada")


## Limitações e observações

- O software pode apresentar dificuldades na análise de textos idiomas diferentes do inglês.
- A metodologia não é livre de falhas, e o valor calculado pode não corresponder adequadamente com o texto analisado em alguns casos.

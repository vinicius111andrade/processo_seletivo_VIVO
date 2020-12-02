# processo_seletivo_VIVO

## Ex 01
Meu algoritmo recebe um array numpy ou um array de arrays numpy, sendo respectivamente a representacao de um vetor e de uma matriz.  
  
Depois ele conta cada ocorrencia dos elementos inteiros pertencentes ao intervalo [0, 15].  
  
E por ultimo retorna um dicionario contabilizando a ocorrencia de cada elemento, com pares no formato elemento : numero_de_ocorrencias.  
  
## Ex 02
Eu usei o flask para criar a API e usei o Insomnia para testa-la.  
  
A API recebe um vetor do tipo [1, 2, 3, 4, ..., 15] em formato de string.  
Ex: http://127.0.0.1:5000/vetor?vetor=%5B0,1,3,4,5%5D  
  
E retorna um arquivo JSON que contabiliza a ocorrencia de cada elemento possivel.  
  
Uma ressalva eh que muito provavelmente essa API nao eh 100% RESTful, nunca havia feito uma API e pelo o que li existem varias restricoes para ela ser RESTful. Espero que se nao estiver de acordo que pelo menos nao esteja muito fora do esperado.  
  
## Ex 03
Nao consegui terminar a tempo, mas vou explicar e mostrar o que fiz.  
  
Com a imagem do log da corrida criei um arquivo .csv, li o arquivo usando pandas, que me retorna um dataframe. Esse dataframe eu uso pra iterar e calcular o que precisa ser calculado, as informacoes de retorno eu armazeno num dicionario.
  
### Como entrar no venv (virtual environment)
https://docs.python.org/pt-br/3/library/venv.html  
  
  Para criar o venv
> python3 -m venv ./venv
  
  Para ativar o venv
> source ./venv/bin/activate

### Como rodar a API
> export FLASK_APP=file_name.py  
> flask run  
  
### Como testar API
Para testar a API estou usando o Insomnia.  
  
### Libs Utilizadas
 - Numpy  
 - Flask
 - Json

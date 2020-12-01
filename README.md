# processo_seletivo_VIVO

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

## Ex 01
Meu algoritmo recebe um array numpy ou um array de arrays numpy, sendo respectivamente a representacao de um vetor e de uma matriz.  
  

  
## Ex 02
Eu usei o flask para criar a API e usei o Insomnia para testa-la.  
  
A API recebe um vetor do tipo [1, 2, 3, 4, ..., 15] em formato de string.
Ex: http://127.0.0.1:5000/vetor?vetor=%5B0,1,3,4,5%5D  
  
E retorna um arquivo JSON que contabiliza a ocorrencia de cada elemento possivel.  
  
## Ex 03
explicar o q fiz
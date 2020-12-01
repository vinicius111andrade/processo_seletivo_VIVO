'''
Transforme o algoritmo anterior em uma API Rest. Você receberá como
parâmetro uma lista com os valores de An e deverá retornar a saída do
algoritmo no formato JSON.
'''

# Recebe uma lista de valores, um vetor
# A saída do algoritmo deve ser no formato JSON

from flask import Flask
from flask import request
import json
import numpy as np

app = Flask(__name__)

# Recebe um dicionário e retorna uma lista com as keys dele.
def		dictionary_keys(dictionary):
	return (list(dictionary))

# Recebe dois dicionários, soma os valores com mesma chave e retorna um dict atualizado.
def		add_occurrences(occurrences, found_elements):
	keys = dictionary_keys(found_elements)
	for key in keys:
		to_add = int(found_elements[key])
		occurrences[key] += to_add
	return occurrences

# Recebe um array e retorna um dicionário com key == elemento, value == número de ocorrências.
def		count_elements(vector):
	occurrences = dict(zip(range(16), [0] * 16))
	unique, counts = np.unique(vector, return_counts=True)
	found_elements = dict(zip(unique, counts))
	occurrences = add_occurrences(occurrences, found_elements)
	return occurrences

# Recebe um array de arrays, itera a matriz chamando count_elements para cada vetor, todas ocorrências são armazenadas num dict que é retornado.
def		iterate_matrix(matrix):
	occurrences = dict(zip(range(16), [0] * 16))
	for i in range(len(matrix)):
		vector = matrix[i]
		new_occurrences = count_elements(vector)
		occurrences = add_occurrences(occurrences, new_occurrences)
	return occurrences

#Checa se uma variavel pode ser convertida pra inteiro
def is_int(arg):
	try:
		int(arg)
		return True
	except:
		return False

# Checa se nao eh string vazia, e se comeca e termina com []
def		basic_input_check(string):
	if len(string) == 0:
		return "Error"
	if string[0] != '[':
		return "Error"
	if string[len(string) - 1] != ']':
		return "Error"
	return 0

# Recebe uma string com formato [0, 1, 2, 3,..., 15]
# Devolve um array com os mesmos elementos ou uma mensagem de erro
def		create_vector(string):
	i = 1
	vetor = np.array([])
	str_nb = ""

	if basic_input_check(string) == "Error":
		return "Error input"

	while string[i] != ']':
		if string[i].isnumeric():
			str_nb += string[i]
		elif string[i] == ',':
			if len(str_nb) == 0 or not is_int(str_nb):
				return "Error empty or not number"
			nb = int(str_nb)
			if nb < 0 or nb > 15:
				return "Error element out of expected interval"
			vetor = np.append(vetor, nb)
			str_nb = ""
		elif string[i] != ' ':
			message = "Error strange char: " + string[i]
			return message
		if string[i + 1] == ']':
			nb = int(str_nb)
			if nb < 0 or nb > 15:
				return "Error element out of expected interval"
			vetor = np.append(vetor, nb)
		i += 1
	return vetor

@app.route('/')
def		instructions():
	ln1 = "<p>Essa API recebe um vetor cujos elementos sao numeros inteiros pertencentes ao intervalo [0, 15].</p>"
	ln2 = "<p>O retorno eh um arquivo Json com o numero de ocorrencias de cada elemento possivel.</p>"
	ln3 = "<p>Para contar as ocorrencias em um vetor usar o path ./vetor</p>"
	ln4 = "<p> vetor = [1, 2, 3, 4, 5, ..., 15]</p>"
	txt = ln1 + ln2 + ln3 + ln4
	return txt

# Recebe um lista de inteiros pertencentes ao intervalo [0,15]
@app.route('/vetor')
def		vector():
	vector_str = request.args.get('vetor')
	vector = create_vector(vector_str)
	if type(vector) == str:
		return vector
	dictionary = count_elements(vector)

	return json.dumps(dictionary)
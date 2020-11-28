import numpy as np

# 2x15 matrix
example_matrix = np.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4], [0, 2, 3, 4, 5, 3, 4, 5, 6, 0, 2, 3, 4, 5, 6])

# contar os elementos de um vetor
# gerar um dict com esses valores
# fazer um merge com um dict maior q vai conter a soma de todos os dicts
# ir pro prox vetor até chegar ao fim da matriz

# Recebe um dicionário e retorna uma lista com as keys dele.
def		dictionary_keys(dictionary):
	return (list(dictionary))

# Recebe um array e retorna um dicionário com key == elemento, value == número de ocorrências.
def		count_elements(vector):
	unique, counts = np.unique(vector, return_counts=True)
	return dict(zip(unique, counts))

# Recebe um dict, uma key e uma lista de valores, se a key não está no dict um par key : lista é criado.
# Por último os novos valores são adicionados à lista e o novo dict é retornado.
def		append_values_in_dict(dictionary, key, list_of_values):
	if key not in dictionary:
		dictionary[key] = list()
	dictionary[key].extend(list_of_values) #se pa vai dar pau pq to passando um int n uma lista como value
	return dictionary

def		combine_dicts(dict1, dict2):
	keys_to_add = dictionary_keys(dict2)
	new_dict = dict1
	for i in range(len(keys_to_add)):
		key = keys_to_add[i]
		new_dict = append_values_in_dict(new_dict, key, dict2[key])
	return new_dict

# Recebe um array de arrays e devolve um dicionário com key == elemento, e value = número de ocorrências.
# Ele chama count_elements várias vezes e retorna a soma total.
def		iterate_matrix(matrix):
	occurrences = {}
	for i in range(len(matrix)):
		partial_occurrences = count_elements(matrix[i])
		occurrences = combine_dicts(dict1, dict2)
	#total_sum = soma_tudo(occurrences)

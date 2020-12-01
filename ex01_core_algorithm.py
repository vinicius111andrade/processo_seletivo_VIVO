import numpy as np

example_matrix = np.array([[0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4], [0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4], [0, 2, 3, 4, 5, 3, 4, 5, 6, 0, 2, 3, 4, 5, 6]])

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

# Itera cada par do dict e printa.
def		output_string(occurrences):
	keys = dictionary_keys(occurrences)
	for key in keys:
		print("Element {:2d} occurred {:2d} times.".format(key, occurrences[key]))

def		main():
	occurrences = iterate_matrix(example_matrix)
	output_string(occurrences)

main()
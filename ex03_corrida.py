from flask import Flask
from flask import request
import json
import numpy as np
import pandas as pd
import datetime

'''
resumo_corrida = {
	"Superman" : {"Tempo Inicial" : tempo, "Total de Voltas" : n_voltas, "Duracao Total" : soma_das voltas, "Velocidade media da corrida" : media_das_medias, "Melhor volta" : melhor_volta},
	...
}

com o n_voltas e a duracao total consigo ordenar quem chegou primeiro e por ultimo

fim_da_corrida = {
	"Ganhador" : nome,
	"Tempo final" : tempo_final
}

com o fim_da_corrida definido eu posso recalcular desconsiderando o q acontecer depois do fim da corrida
'''
# acha um heroi, procura todas as ocorrencias desse heroi, preenche o dict acima
# vai pro prox heroi ate terminar o df
# retorna uma tabela em html bonitinha

# Para reutilizar esse template dict2 = dict1.copy()
resumo_template = {
	"Tempo Inicial" : 0,
	"Total de Voltas" : 0,
	"Duracao Total" : 0,
	"Velocidade media da corrida" : 0,
	"Melhor volta" : 0
	}

def		gera_resumo_heroi(df, super_heroi):
	resumo_heroi = resumo_template.copy()
	duracao_total = datetime.datetime.strptime('0:0.0', '%M:%S.%f')

	for index, row in df.iterrows():
		if row["Super-Heroi"] == super_heroi:
			if row["Numero Volta"] == 1:
				resumo_heroi["Tempo Inicial"] = row["Hora"]
			if int(row["Numero Volta"]) > resumo_heroi["Total de Voltas"]:
				resumo_heroi["Total de Voltas"] = row["Numero Volta"]
			duracao_total += datetime.datetime.strptime(row["Tempo Volta"], '%M:%S.%f')
	resumo_heroi["Duracacao Total"] = duracao_total
	return resumo_heroi

def		gera_resumo_corrida(df):
	resumo_corrida = {}

	for index, row in df.iterrows():
		super_heroi = row["Super-Heroi"]
		if not super_heroi in resumo_corrida:
			print(super_heroi)
			resumo_corrida[super_heroi] = gera_resumo_heroi(df, super_heroi)

	return resumo_corrida

# primeiro ele checa se o suprheroi ja esta no dict, se n tiver ele adiciona e calcula tudo
# vai pra proxima linha e repete ate o fim
# quando terminar calcula o vencedor
# repete o processo pra fazer os calculos mas soh pros dados gerados durante a corrida, que acaba quando o vencedor termina a prova

def		main():
	df = pd.read_csv("log_corrida.csv")
	print(gera_resumo_corrida(df))
	print(df)

main()
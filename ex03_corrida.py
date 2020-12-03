from flask import Flask
from flask import request
import json
import numpy as np
import pandas as pd
from datetime import timedelta

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

def		inicio_em_segundos(tempo):
	hrs, mins, secs, millis = map(float, tempo.split('.'))
	td = timedelta(hours=hrs, minutes=mins, seconds=secs, milliseconds=millis)
	return td.total_seconds()

def		volta_em_segundos(tempo):
	mins, secs, millis = map(float, tempo.split('.'))
	td = timedelta(minutes=mins, seconds=secs, milliseconds=millis)
	return td.total_seconds()

def		gera_resumo_heroi(df, super_heroi):
	resumo_heroi = resumo_template.copy()
	duracao_total = 0
	menor_volta_seg = 999999999
	soma_velo_medias = 0

	for index, row in df.iterrows():
		if row["Super-Heroi"] == super_heroi:
			volta_seg = volta_em_segundos(row["Tempo Volta"])
			velocidade_m = float(row["Velocidade media da Volta"])
			duracao_total += volta_seg
			soma_velo_medias += velocidade_m

			if row["Numero Volta"] == 1:
				resumo_heroi["Tempo Inicial"] = row["Hora"]
			if int(row["Numero Volta"]) > resumo_heroi["Total de Voltas"]:
				resumo_heroi["Total de Voltas"] = int(row["Numero Volta"])
			if menor_volta_seg > volta_seg:
				menor_volta_seg = volta_seg
				resumo_heroi["Melhor volta"] = row["Numero Volta"]
	resumo_heroi["Duracao Total"] = duracao_total
	resumo_heroi["Velocidade media da corrida"] = soma_velo_medias / resumo_heroi["Total de Voltas"]
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
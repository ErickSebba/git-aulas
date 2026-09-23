import json
from config import ARQUIVO_TAREFAS


def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo)


def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def exportar_tarefas_txt(tarefas, caminho="tarefas.txt"):
    with open(caminho, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa}\n")

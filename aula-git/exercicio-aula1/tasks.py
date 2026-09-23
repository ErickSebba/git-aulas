from utils import formatar_tarefa

tarefas = []


def adicionar_tarefa(texto):
    tarefas.append(texto)


def remover_tarefa(indice):
    tarefas.pop(indice - 1)


def listar_tarefas():
    for indice, tarefa in enumerate(tarefas, start=1):
        print(formatar_tarefa(indice, tarefa))

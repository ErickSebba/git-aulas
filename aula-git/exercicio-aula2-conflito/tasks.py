tarefas = [
    "Estudar Git",
    "Fazer exercicio de merge",
    "Revisar pull requests"
]


def listar_tarefas():
    print("Tarefas pendentes:")
    for tarefa in tarefas:
        print(f"- {tarefa}")


def adicionar_tarefa(nome):
    tarefas.append(nome)
    print(f"Tarefa adicionada: {nome}")


listar_tarefas()

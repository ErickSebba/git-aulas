tarefas = []


def adicionar_tarefa(nome):
    tarefas.append(nome)
    print(f"Tarefa adicionada: {nome}")


def remover_tarefa(nome):
    tarefas.remove(nome)
    print(f"Tarefa removida: {nome}")


def listar_tarefas():
    print("Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


adicionar_tarefa("Estudar Git")
adicionar_tarefa("Fazer compras")
listar_tarefas()

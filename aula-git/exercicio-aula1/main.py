from tasks import adicionar_tarefa, remover_tarefa, listar_tarefas
from storage import salvar_tarefas, carregar_tarefas

tarefas_salvas = carregar_tarefas()

adicionar_tarefa("Estudar Git")
adicionar_tarefa("Fazer exercicio da aula 1")
listar_tarefas()

salvar_tarefas(tarefas_salvas)

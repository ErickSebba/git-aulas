# AulaGIT

Material de apoio para uma aula introdutória de Git. Contém dois projetos de exemplo, cada um com um propósito diferente.

## Estrutura

```
AulaGIT/
├── demo-git/          # Demonstração guiada (comandos básicos de Git)
└── exercicio-aula1/   # Exercício prático (repositório com problemas para corrigir)
```

## demo-git

Projeto simples de lista de tarefas em Python (`tasks.py`), usado para demonstrar ao vivo, passo a passo, o fluxo básico do Git:

- `git init`, `git status`, `git add`, `git commit`, `git log`
- Diferença entre mudanças não staged e staged (`git diff` vs `git diff --staged`)
- Uso de `.gitignore` para excluir `.env` e `__pycache__/` do rastreamento

Use este projeto para mostrar o "caminho feliz": cada comando é executado em ordem e o resultado é sempre o esperado.

## exercicio-aula1

Projeto de lista de tarefas em Python (5 arquivos: `main.py`, `tasks.py`, `storage.py`, `utils.py`, `config.py`), montado propositalmente com problemas comuns de quem está aprendendo Git. Os alunos devem identificar e corrigir:

1. **Mudanças misturadas no diretório de trabalho** — uma correção de bug em `tasks.py` e uma função nova em `storage.py`, ainda não commitadas nem staged. Exercício: separar em dois commits distintos e coerentes.
2. **Arquivos que não deveriam estar versionados** — `.env` e `__pycache__/` já rastreados desde o primeiro commit, sem `.gitignore`. Exercício: criar o `.gitignore` correto e destrackear os arquivos sem apagá-los do disco (`git rm -r --cached`).
3. **Um commit malfeito no histórico** — mensagem vaga (`"mudanças"`) misturando duas alterações sem relação entre si em arquivos diferentes. Serve apenas como exemplo de contraste; não precisa ser desfeito.

Use este projeto para a parte prática da aula, distribuindo o repositório (incluindo a pasta `.git`) para os alunos resolverem.

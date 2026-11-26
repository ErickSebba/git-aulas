# Minicurso de Git e GitHub

Material prático de um minicurso introdutório de Git e GitHub que eu ministrei em 2026: projetos
de exemplo para demonstrar os comandos ao vivo, repositórios montados com problemas para os alunos
corrigirem, páginas para visualizar branches e listas de exercícios.

## Conteúdo

| Pasta | O que é |
|---|---|
| `aula-git/demo-git/` | lista de tarefas em Python para demonstrar o fluxo básico ao vivo: `init`, `status`, `add`, `commit`, `log`, `diff` × `diff --staged` e `.gitignore` |
| `aula-git/exercicio-aula1/` | projeto montado de propósito com erros comuns (mudanças misturadas, `.env` e `__pycache__/` versionados, commit vago) para os alunos separarem commits e corrigirem com `git rm -r --cached` |
| `aula-git/exercicio-aula2-conflito/` | arquivo preparado para provocar e resolver um conflito de merge |
| `aula-git/demo-aula2-comandos/`, `aula-git/demo-branches-visual/` | páginas HTML simples usadas para mostrar branches e merge de forma visual |
| `aula-git/aula2-exercicios.md` | exercícios da aula 2 (branches e merge na prática) |
| `material-minicurso/exercicios-minicurso.md` | exercícios da aula 1: fundamentos, comandos essenciais e o primeiro repositório |

## Como usar

Os exercícios funcionam melhor quando cada aluno recebe a pasta do projeto e trabalha nela com o
terminal ou o VS Code. Para o `exercicio-aula1`, distribua a pasta já com o histórico de commits
problemático e peça para os alunos arrumarem o repositório seguindo `aula-git/README.md`.

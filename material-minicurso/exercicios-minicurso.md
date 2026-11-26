# Minicurso de Git e GitHub — Exercícios

## Aula 1 — Fundamentos e Comandos Essenciais

### 1. Recapitulação dos Tópicos

* **Controle de Versão**: sistema que registra alterações em arquivos ao longo do tempo, permitindo recuperar versões anteriores e organizar o trabalho colaborativo.
* **Sistemas Centralizados vs. Distribuídos**:
  * Centralizado: um único servidor guarda o histórico; desenvolvedores obtêm apenas a versão mais recente.
  * Distribuído (Git): cada desenvolvedor possui uma cópia completa do repositório, incluindo todo o histórico.
* **Modelo de Dados do Git — os três estados**:
  * *Working Directory*: onde os arquivos são editados diretamente.
  * *Staging Area*: onde ficam as alterações selecionadas para o próximo commit.
  * *Repositório (.git)*: onde as alterações são permanentemente registradas via commits.
* **Comandos essenciais**:
  * `git init`: cria um novo repositório.
  * `git status`: mostra o estado atual do diretório de trabalho e da área de preparação.
  * `git add`: move alterações do diretório de trabalho para a staging area.
  * `git diff` / `git diff --staged`: mostra diferenças não preparadas / já preparadas.
  * `git commit`: registra permanentemente as alterações preparadas.
  * `git log` / `git log --oneline --graph`: exibe o histórico de commits.
* **.gitignore**: arquivo de configuração que informa ao Git quais arquivos ou pastas nunca devem ser rastreados (ex.: `.env`, `node_modules/`).
* **Boas práticas de commit**: mensagens claras e no modo imperativo; um commit deve representar uma única unidade lógica de alteração (granularidade).
* **Repositórios remotos (prévia conceitual)**:
  * `git clone`: copia um repositório remoto existente para a máquina local.
  * `git push`: envia commits locais para o repositório remoto.
  * `git pull`: busca e integra alterações do repositório remoto ao repositório local.

### 2. Exercícios Práticos

* **Atividade Guiada: Primeiro Repositório**
  * Objetivo: introduzir na prática os três estados do Git e observar o efeito de cada comando sobre o diretório de trabalho.
  * Passo a passo: criar pasta → `git init` → criar arquivos → `git add` → `git commit` → editar → `git diff` → configurar `.gitignore` → `git log --graph`.

* **Exercício 1: Organizando um Repositório Mal Estruturado**
  * Objetivo: praticar separação de commits, configuração de `.gitignore` e remoção de arquivos indevidamente rastreados.
  * Passo a passo: identificar alterações misturadas no diretório de trabalho → separá-las em commits distintos e bem descritos → criar `.gitignore` adequado → remover do rastreamento os arquivos que não deveriam estar lá.

---

### Atividade Guiada: Primeiro Repositório

Nesta atividade, toda a turma acompanha em conjunto (live coding) a criação de um repositório do zero, executando cada comando essencial e observando, passo a passo, como o Git reage ao diretório de trabalho. O objetivo é fixar visualmente o modelo dos três estados antes de os alunos partirem para o exercício prático avaliado.

#### Objetivo do Exercício

* Observar como `git status` muda de resposta após cada ação (criação de arquivo, `add`, `commit`, edição).
* Compreender na prática a diferença entre arquivo *untracked*, *staged* e *committed*.
* Ver o efeito real de um `.gitignore` sobre arquivos já existentes no diretório.

#### Descrição da Atividade

1. Criar uma pasta vazia `meu-primeiro-repo` e entrar nela.
2. Rodar `git init` e em seguida `git status`.
3. Criar um arquivo `index.html` com conteúdo qualquer e rodar `git status` novamente.
4. Rodar `git add index.html` e conferir a mudança de estado com `git status`.
5. Criar um segundo arquivo `style.css` sem dar `add`, e observar os dois estados coexistindo no `git status`.
6. Rodar `git add .` e conferir que ambos os arquivos estão staged.
7. Rodar `git commit -m "feat: cria estrutura inicial da página"`, depois `git status` e `git log`.
8. Editar `index.html` (mudança pequena) e observar o arquivo como *modified* no `git status`; rodar `git diff`.
9. Rodar `git add index.html` e comparar `git diff` (vazio) com `git diff --staged` (mostra a mudança).
10. Rodar `git commit -m "style: ajusta texto do título"` e conferir `git log --oneline`.
11. Criar `.gitignore` contendo `*.log`, depois criar um arquivo `debug.log`; rodar `git status` e observar que o arquivo não aparece.
12. Rodar `git log --oneline --graph` para fechar, revisando toda a linha do tempo criada.

#### Comandos e Estados Esperados

```bash
mkdir meu-primeiro-repo && cd meu-primeiro-repo
git init
git status
# → "nothing to commit" (repositório vazio)

echo "<h1>Olá</h1>" > index.html
git status
# → index.html aparece como untracked

git add index.html
git status
# → index.html aparece como staged (to be committed)

echo "body { color: black; }" > style.css
git status
# → index.html staged, style.css untracked (dois estados ao mesmo tempo)

git add .
git status
# → ambos staged

git commit -m "feat: cria estrutura inicial da página"
git status
# → working tree clean
git log
# → mostra o commit criado

# edita index.html (ex: muda o texto do <h1>)
git status
# → index.html aparece como modified
git diff
# → mostra a alteração linha a linha

git add index.html
git diff
# → vazio (não há mais diferença não staged)
git diff --staged
# → mostra a mesma alteração, agora staged

git commit -m "style: ajusta texto do título"
git log --oneline
# → 2 commits

echo "*.log" > .gitignore
touch debug.log
git status
# → debug.log NÃO aparece na lista (ignorado)

git log --oneline --graph
# → linha do tempo completa da atividade
```

---

### Exercício 1: Organizando um Repositório Mal Estruturado

Nesta atividade prática, os alunos recebem um repositório já existente, mas organizado de forma incorreta — simulando um projeto real que cresceu sem cuidado com o versionamento. O objetivo é aplicar os conceitos de staging, commits atômicos, mensagens de commit e `.gitignore` para corrigir o histórico e o estado do repositório.

#### Objetivo do Exercício

* Separar alterações não relacionadas em commits distintos e bem descritos.
* Identificar arquivos que nunca deveriam ter sido versionados e removê-los do rastreamento sem apagá-los do disco.
* Praticar a leitura de `git status` e `git diff` para entender o estado de um repositório desconhecido antes de agir.

#### Descrição da Tarefa

1. Explorar o repositório recebido com `git log` e `git status` para entender o estado atual, antes de qualquer alteração.
2. Identificar, no diretório de trabalho, duas mudanças não relacionadas (ex.: uma correção de bug em um arquivo e uma nova função em outro) e separá-las em dois commits distintos, cada um com mensagem clara e no modo imperativo.
3. Localizar os arquivos indevidamente rastreados desde o commit inicial (ex.: `.env`, pasta de cache/dependências) e criar um `.gitignore` adequado para eles.
4. Remover esses arquivos do rastreamento do Git com `git rm --cached`, mantendo-os no disco.
5. Conferir o resultado final com `git log --oneline` e `git status`, garantindo um histórico limpo e um diretório de trabalho sem pendências.

#### Estado Inicial do Repositório / Comandos Esperados (gabarito)

```bash
# --- Estado inicial recebido pelo aluno ---
git log --oneline
# a1b2c3d "mudanças"   ← commit inicial mal descrito, mistura funcionalidades

git status
# Untracked/modified:
#   bugfix em arquivo_a (não commitado)
#   nova função em arquivo_b (não commitado)
# Tracked incorretamente:
#   .env
#   __pycache__/ (ou node_modules/, conforme o projeto)

# --- Passo a passo esperado da correção ---

# 1) Separar as duas mudanças em commits distintos
git add arquivo_a
git commit -m "fix: corrige [descrição do bug]"

git add arquivo_b
git commit -m "feat: adiciona [descrição da função]"

# 2) Criar o .gitignore adequado
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .gitignore
git commit -m "chore: adiciona .gitignore para arquivos sensíveis e de cache"

# 3) Remover do rastreamento os arquivos que já estavam versionados
git rm --cached .env
git rm --cached -r __pycache__
git commit -m "chore: remove arquivos sensíveis e de cache do rastreamento"

# --- Estado final esperado ---
git log --oneline
# deve mostrar 4 commits novos, cada um com escopo único e mensagem clara

git status
# → working tree clean, .env e __pycache__/ não aparecem mais
```

> Observação para o instrutor: o commit inicial "mudanças" é proposital — serve de contraste com as boas práticas ensinadas na Aula 1 e não precisa ser reescrito nesta atividade (reescrita de histórico é tema de aulas futuras).

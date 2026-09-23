# Aula 2 — Exercícios Práticos (versão com arquivos .txt)

> Mesma estrutura e objetivos da versão anterior, adaptada para usar arquivos de texto simples em vez de HTML. O Exercício 2 já usava `arquivo.txt`, então mudou pouco. A Atividade Guiada agora usa **dois arquivos txt** (`projeto.txt` e `rodape.txt`) — isso também deixa mais visível a diferença entre "editar um arquivo existente" e "criar um arquivo novo numa branch", que é um ótimo gancho para explicar isolamento de branches.

---

## Atividade Guiada — Branches e Merge na Prática

### Objetivo do Exercício
- Sentir a isolação entre branches e o comportamento do diretório de trabalho ao alternar entre elas.
- Observar a diferença no histórico (`git log --graph`) entre merge Fast-Forward e Three-Way Merge.
- Praticar a exclusão segura de branches mescladas.

> ⚠️ **Preparação:** antes de começar, rode `git branch`. Se a branch atual não se chamar `main` (em instalações mais antigas o padrão é `master`), rode `git branch -m main` para renomear, ou configure de uma vez para toda a aula com `git config --global init.defaultBranch main`. Sem isso, os passos "`git switch main`" mais adiante falham com `fatal: invalid reference: main`.

### Arquivo base — `projeto.txt`

```
Titulo: Projeto Demonstracao
Descricao: Material de apoio para a aula de Git.
Autor: Turma de Introducao ao Git
```

### Descrição do Passo a Passo
1. Em um repositório existente ou novo (com a branch `main` já confirmada e `projeto.txt` já commitado), executar `git branch` para verificar que apenas a branch `main` existe.
2. Criar e trocar para uma nova branch com `git switch -c feature-rodape`.
3. Criar um **arquivo novo** `rodape.txt` (com informações de contato) e realizar um commit. Executar `git log --oneline --graph --all` para ver a branch avançando sozinha enquanto a `main` fica parada.
4. Voltar para a `main` com `git switch main` e notar que `rodape.txt` **desaparece completamente** do diretório (demonstrando a isolação de branches de forma ainda mais visível do que uma simples edição de linha).
5. Mesclar a alteração com `git merge feature-rodape` e observar o comportamento Fast-Forward (a `main` apenas avança o ponteiro, sem criar um commit de merge, e `rodape.txt` passa a existir na `main`).
6. Deletar a branch mesclada com `git branch -d feature-rodape`.
7. Criar uma nova branch `feature-titulo` a partir da `main` atual e editar a **primeira linha** de `projeto.txt` (o título), depois commitar.
8. Voltar para a `main` e editar uma linha **diferente** de `projeto.txt` (ex.: a linha de descrição ou uma nova linha de nota), para que as duas branches divirjam sem se sobrepor.
9. Executar `git merge feature-titulo` a partir da `main`. Notar que dessa vez NÃO é Fast-Forward; o Git abre o editor pedindo uma mensagem para o commit de merge (Three-Way Merge).
10. Executar `git log --oneline --graph` para observar visualmente a estrutura de junção do histórico.

### Comandos e Estados Esperados

```
git branch
# -> Lista as branches locais existentes. O asterisco (*) e o destaque indicam que estamos
#    atualmente na branch 'main' e que a referência especial HEAD aponta para ela.

git switch -c feature-rodape
# -> Cria a nova branch chamada 'feature-rodape' a partir do estado atual da 'main' e
#    imediatamente alterna o HEAD para ela (equivalente a git checkout -b feature-rodape).

echo "Contato: suporte@empresa.com" > rodape.txt
git add rodape.txt
git commit -m "feat: adiciona arquivo de rodape com contato"
# -> Cria um arquivo NOVO (rodape.txt não existia antes, então usar "> " aqui é seguro —
#    não há conteúdo anterior para perder). Adiciona à Staging Area e grava um novo commit.
#    O ponteiro da branch 'feature-rodape' avança 1 commit à frente da 'main', que
#    permanece inalterada e sem esse arquivo.

git log --oneline --graph --all
# -> Exibe o gráfico visual de todo o histórico do repositório incluindo todas as branches
#    (--all). É possível notar o ponteiro 'feature-rodape' um commit à frente da 'main'.

git switch main
ls
# -> Move o ponteiro HEAD de volta para a branch 'main'. O Git restaura automaticamente os
#    arquivos do Working Directory para o estado gravado na 'main' — como 'rodape.txt' foi
#    criado só na outra branch, ele literalmente SOME da pasta. É a demonstração mais
#    direta possível de que branches isolam o diretório de trabalho.

git merge feature-rodape
# -> Realiza a mesclagem da 'feature-rodape' na 'main'. Como a branch 'main' não recebeu
#    nenhum commit novo desde que 'feature-rodape' foi criada, o Git executa um merge do
#    tipo Fast-Forward: simplesmente desloca o ponteiro da 'main' para frente até alcançar
#    o mesmo commit de 'feature-rodape' — sem criar um novo commit de fusão. 'rodape.txt'
#    volta a aparecer, agora também na 'main'.

git branch -d feature-rodape
# -> Remove com segurança a branch 'feature-rodape'. O parâmetro -d só permite a exclusão
#    se todas as alterações da branch já tiverem sido devidamente mescladas (como feito no
#    passo anterior). Apenas o ponteiro da branch é removido; o histórico e o rodape.txt
#    permanecem intactos na 'main'.

git switch -c feature-titulo
```

```
# (Ação do Aluno: Edição Manual)
# -> Abrir projeto.txt no editor e trocar SÓ a primeira linha:
#      Titulo: Projeto Demonstracao
#    por:
#      Titulo: Meu Projeto Incrivel
#    Não usar "echo ... > projeto.txt" aqui — isso sobrescreveria o arquivo inteiro e
#    apagaria as outras duas linhas. Edição manual de uma linha específica é o jeito
#    seguro (e o mais realista: é assim que se edita código no dia a dia).
```

```
git add projeto.txt
git commit -m "feat: atualiza titulo do projeto"
# -> A branch 'feature-titulo' agora está 1 commit à frente da 'main', com a mudança
#    isolada na linha do título.

git switch main
```

```
# (Ação do Aluno: Edição Manual, ou via terminal com >> pois é só um acréscimo)
echo "Nota: revisado para a aula 2" >> projeto.txt
git add projeto.txt
git commit -m "docs: adiciona nota de revisao ao projeto"
# -> Retorna para a 'main' e acrescenta uma linha NOVA ao final (">>", não "> "), em uma
#    parte diferente do arquivo da que foi alterada em 'feature-titulo'. Agora ocorreu uma
#    divergência real: tanto a 'main' quanto a 'feature-titulo' possuem commits exclusivos
#    criados após o ponto de bifurcação comum — mas em linhas diferentes, então não há
#    conflito.

git merge feature-titulo
# -> Inicia o merge da 'feature-titulo' na 'main'. Como ambas as branches possuem
#    históricos divergentes, o Git NÃO pode realizar um Fast-Forward. Ele executa o
#    algoritmo Three-Way Merge (comparando o commit do topo da main, o commit do topo da
#    feature e o ancestral comum das duas branches) e abre o editor de texto padrão
#    solicitando a confirmação da mensagem do novo "Commit de Merge" automático.
#
#    *** Atenção: se core.editor não estiver configurado, o Git normalmente abre o Vim por
#    padrão, o que trava alunos que nunca usaram um editor modal. Duas saídas:
#    (a) antes da aula, configurar em cada máquina: git config --global core.editor "notepad"
#        (ou o editor de preferência da turma);
#    (b) ou avisar antecipadamente: se o Vim abrir, digite :wq e pressione Enter para salvar
#        e sair, aceitando a mensagem padrão do merge. ***

git log --oneline --graph
# -> Exibe o gráfico do histórico consolidado. O parâmetro --graph desenha as linhas do
#    tempo mostrando a bifurcação que ocorreu e o ponto exato de junção criado pelo commit
#    de merge (diferente do merge Fast-Forward do passo 5, que manteve uma linha reta pura).
```

---

## Exercício 2 — Resolvendo um Conflito de Merge

Nesta atividade, os alunos recebem um repositório com duas branches que já divergiram na mesma linha do mesmo arquivo. O objetivo é resolver o conflito manualmente e, em seguida, repetir o processo usando rebase em uma cópia limpa para comparar o resultado final.

### Objetivo do Exercício
- Reconhecer os marcadores de conflito (`<<<<<<<`, `=======`, `>>>>>>>`) e compreender o que cada lado representa.
- Resolver o conflito manualmente, escolhendo ou combinando o conteúdo correto.
- Comparar a experiência de resolução de conflito via merge e via rebase.

### Arquivo base — `arquivo.txt`

Já é um arquivo de texto simples — nenhuma mudança de formato necessária aqui. Ex.: um arquivo curto de 15-20 linhas (lista de tarefas, notas de projeto, etc.) onde a mesma linha é alterada de formas diferentes em `main` e `branch-b`.

### Descrição da Tarefa
1. Explorar o repositório com `git log --oneline --graph --all` para visualizar as duas branches divergentes.
2. Tentar `git merge branch-b` a partir da `main` e observar a mensagem de conflito exibida pelo Git.
3. Abrir o arquivo conflitante, identificar os marcadores de conflito e editá-lo manualmente para obter o conteúdo final desejado.
4. Adicionar o arquivo alterado com `git add` e rodar `git commit` para concluir o merge.
5. Em uma cópia limpa do repositório, executar `git switch branch-b` e `git rebase main`. Resolver o conflito da mesma forma, rodar `git add` e dar sequência com `git rebase --continue`.
6. Comparar o histórico final dos dois cenários através do `git log --oneline --graph`.

### Comandos Esperados / Gabarito

```
# --- Cenário 1: Resolução de Conflito via Merge ---

git log --oneline --graph --all
# -> Inspeciona a árvore completa do repositório. O gráfico exibe a branch 'main' e a
#    'branch-b' divergindo a partir de um commit ancestral comum, cada uma com
#    modificações na mesma linha do arquivo.txt.
# * (branch-b) commit alterando linha X do arquivo.txt
# | * (main) commit alterando a MESMA linha X do arquivo.txt
# |/
# * commit base comum

git merge branch-b
# -> Tenta mesclar a 'branch-b' na branch atual ('main'). O Git tenta unir as alterações
#    automaticamente, mas identifica que a mesma linha do arquivo.txt foi modificada de
#    formas diferentes nas duas branches. O processo de fusão é interrompido com o aviso
#    "CONFLICT (content): Merge conflict in arquivo.txt" e o repositório entra em estado
#    de merge não finalizado (git status mostra "You have unmerged paths").

cat arquivo.txt
# -> Exibe o conteúdo do arquivo no terminal contendo os marcadores de conflito inseridos
#    automaticamente pelo Git para delimitar os trechos incompatíveis:
# <<<<<<< HEAD
# conteúdo da main (código da branch atual em que você está posicionado)
# ======= (linha separadora entre as duas propostas de código)
# conteúdo da branch-b (código vindo da branch que está sendo mesclada)
# >>>>>>> branch-b

# (Ação do Aluno: Edição Manual)
# -> O aluno abre o arquivo no seu editor de código (ex: VS Code), analisa as duas
#    versões, exclui os marcadores de conflito (<<<<<<<, =======, >>>>>>>) e edita o
#    texto para manter apenas a versão correta ou a união coerente de ambas.

git add arquivo.txt
# -> Move o arquivo.txt já corrigido para a Staging Area (Index). Esse passo sinaliza
#    formalmente ao Git que o conflito existente naquele arquivo específico foi
#    completamente resolvido pelo usuário.

git commit -m "fix: resolve conflito de mesclagem entre main e branch-b"
# -> Finaliza o processo de merge gravando um novo Commit de Merge que consolida a
#    resolução do conflito e encerra o estado de merge, deixando a Working Tree limpa.

# --- Cenário 2: Resolução do Mesmo Conflito via Rebase (em uma cópia limpa do repositório) ---

git switch branch-b
# -> Alterna para a 'branch-b', que é a branch cujos commits queremos reescrever e
#    posicionar no topo da 'main'.

git rebase main
# -> Inicia o Rebase. O Git temporariamente retira os commits da 'branch-b' e tenta
#    reaplicar os commits um a um sobre o commit mais recente da 'main'. Ao tentar
#    reaplicar o commit conflitante da 'branch-b', o Git detecta o mesmo conflito de
#    conteúdo e pausa o processo.
#
#    *** Terminologia (Git >= 2.26, inclui qualquer instalação recente): o `git status`
#    mostra "interactive rebase in progress" e a pasta interna usada é
#    ".git/rebase-merge" — não existe mais o estado "REBASE-APPLY" por padrão (isso só
#    aparece se alguém forçar com "git rebase --apply", modo antigo). Não muda nada nos
#    comandos que o aluno digita, é só terminologia caso apareça no git status. ***

cat arquivo.txt
# -> Exibe os mesmos marcadores de conflito (<<<<<<<, =======, >>>>>>>) no arquivo.txt.
#    O lado HEAD agora representa a 'main' (que é a base sobre a qual estamos aplicando os
#    commits), e a parte inferior representa o commit da 'branch-b' sendo reaplicado.

# (Ação do Aluno: Edição Manual)
# -> O aluno edita manualmente o arquivo no editor, remove todas as linhas marcadoras de
#    conflito e salva o arquivo com a versão final desejada.

git add arquivo.txt
# -> Prepara o arquivo corrigido na Staging Area para confirmar a resolução do conflito
#    deste passo do rebase.

git rebase --continue
# -> Instrui o Git a continuar o processo de Rebase. O Git reescreve o commit da
#    'branch-b' no topo do último commit da 'main' utilizando o conteúdo resolvido. Não é
#    criado nenhum commit de merge extra, e normalmente não abre editor (reaproveita a
#    mensagem original do commit que está sendo reaplicado).

git log --oneline --graph
# -> Inspeciona o histórico resultante. Diferente do Cenário 1 (Merge), onde o gráfico
#    exibe um nó visual de bifurcação e junção, o Rebase gera um histórico perfeitamente
#    linear, como se todo o trabalho da 'branch-b' tivesse sido desenvolvido diretamente
#    após o último commit da 'main'.
```

---

## Versões resumidas (para slide/consulta rápida)

### Atividade Guiada: Branches e Merge na Prática
**Objetivo:** Sentir a isolação entre branches e entender na prática a diferença entre merge Fast-Forward e Three-Way Merge.

**Passo a passo:** confirmar que a branch é `main` → `git branch` → `git switch -c feature-rodape` → criar arquivo novo `rodape.txt` e commitar → `git switch main` (rodape.txt some) → `git merge feature-rodape` (Fast-Forward, rodape.txt reaparece) → `git branch -d feature-rodape` → criar `feature-titulo` → editar a 1ª linha de `projeto.txt` e commitar → `git switch main` → editar outra linha de `projeto.txt` e commitar → `git merge feature-titulo` (Three-Way Merge — atenção ao editor que abre, geralmente Vim) → observar no `git log --graph`.

### Exercício 2: Resolvendo um Conflito de Merge
**Objetivo:** Reconhecer marcadores de conflito, resolver conflitos manualmente e comparar a experiência de resolução via merge e via rebase.

**Passo a passo:** analisar repositório divergente (`arquivo.txt`) → tentar `git merge branch-b` → identificar marcadores (`<<<<<<<`, `=======`, `>>>>>>>`) → editar arquivo e commitar → repetir processo em cópia limpa via `git rebase main` (estado interno é "rebase em andamento", não "REBASE-APPLY" nesta versão do Git).

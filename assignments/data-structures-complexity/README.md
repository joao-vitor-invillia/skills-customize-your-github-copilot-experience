# 📘 Atividade: Estruturas de Dados e Complexidade em Python

## 🎯 Objetivo

Nesta atividade, você vai praticar a escolha de estruturas de dados adequadas e comparar desempenho de soluções em Python. Ao final, você deverá justificar tecnicamente por que uma abordagem é mais eficiente que outra em cenários diferentes.

## 📝 Tarefas

### 🛠️ Implementar Estruturas de Dados de Apoio

#### Descrição
Implemente utilitários com listas, dicionários, pilha e fila para resolver operações comuns de busca e histórico de ações.

#### Requisitos
O programa concluído deve:

- Implementar uma pilha (`push`, `pop`) para histórico de operações.
- Implementar uma fila (`enqueue`, `dequeue`) para processar requisições em ordem FIFO.
- Criar uma função de contagem de frequência de elementos usando `dict`.
- Garantir que operações inválidas (como remover de pilha/fila vazia) sejam tratadas sem quebrar o programa.

### 🛠️ Resolver Problemas com Estratégias Diferentes

#### Descrição
Resolva o mesmo problema com duas abordagens: uma solução ingênua e outra otimizada com estrutura de dados apropriada.

#### Requisitos
O programa concluído deve:

- Implementar busca de duplicatas em lista com abordagem O(n²).
- Implementar a mesma busca com `set` ou `dict` em O(n).
- Implementar busca de elementos por chave em uma coleção usando lista e usando dicionário.
- Exibir no terminal os resultados das duas abordagens para o mesmo conjunto de dados.

### 🛠️ Medir e Comparar Complexidade na Prática

#### Descrição
Crie um experimento simples para medir tempo de execução e comparar as abordagens implementadas.

#### Requisitos
O programa concluído deve:

- Gerar entradas de tamanhos diferentes (por exemplo: 1.000, 5.000 e 10.000 itens).
- Medir tempo de execução com `time.perf_counter()` para cada abordagem.
- Exibir uma tabela simples com tamanho da entrada, tempo e abordagem.
- Escrever uma conclusão curta explicando quando cada estrutura de dados é mais indicada.

# 📘 Tarefa: Building REST APIs with FastAPI

## 🎯 Objective

Nesta atividade, você vai construir uma API REST com FastAPI, aplicando rotas, validação com Pydantic, códigos de status HTTP e operações CRUD em memória.

## 📝 Tasks

### 🛠️ Criar a Estrutura Base da API

#### Descrição
Configure a aplicação FastAPI e implemente endpoints iniciais para verificar se o servidor está ativo.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` no arquivo `starter-code.py`.
- Implementar um endpoint `GET /health` que retorne um JSON com status `ok`.
- Implementar um endpoint `GET /` com uma mensagem curta de boas-vindas da API.

### 🛠️ Implementar CRUD de Tarefas

#### Descrição
Crie uma coleção em memória para armazenar tarefas e implemente os endpoints principais de CRUD.

#### Requisitos
O programa concluído deve:

- Definir modelos Pydantic para criação e resposta de tarefas.
- Implementar `POST /tasks` para criar tarefa com `title` obrigatório e `done` opcional.
- Implementar `GET /tasks` para listar todas as tarefas.
- Implementar `GET /tasks/{task_id}` retornando 404 quando a tarefa não existir.
- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa e retornar status `204`.

### 🛠️ Adicionar Validação e Tratamento de Erros

#### Descrição
Aprimore a API com validações de entrada e respostas de erro claras.

#### Requisitos
O programa concluído deve:

- Validar que `title` tenha pelo menos 3 caracteres.
- Retornar erros HTTP apropriados (`400` ou `404`) com mensagens explicativas.
- Garantir que IDs inválidos ou inexistentes não quebrem a aplicação.
- Testar manualmente os endpoints com Swagger em `/docs`.

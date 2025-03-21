# TesteSoftware-Farmacia-
# Plano de Teste - Sistema de Controle de Farmácia

## Versão 1.0

### Histórico de Alterações

| Data       | Versão | Descrição            | Autor(a)                    |
| ---------- | ------ | -------------------- | --------------------------- |
| 14/03/2025 | 1.0    | Criação do documento | Lois Miguel e Matheus Lucas |

---

## 1. Introdução

Este documento apresenta o plano de teste do **Sistema de Controle de Farmácia**, abordando os requisitos a serem testados, estratégias de teste, tipos de teste aplicados, recursos necessários e cronograma das atividades de teste.

O objetivo principal é garantir que todas as funcionalidades do sistema operem corretamente, com desempenho adequado e segurança para os dados.

---

## 2. Requisitos a Testar

### 2.1 Casos de Uso

| Identificador | Nome do Caso de Uso      |
| ------------- | ------------------------ |
| UC1           | Cadastro de Medicamentos |
| UC2           | Venda de Medicamentos    |
| UC3           | Controle de Estoque      |
| UC4           | Geração de Relatórios    |

### 2.2 Requisitos Não Funcionais

| Identificador | Nome do Requisito |
| ------------- | ----------------- |
| RNF1          | Desempenho        |
| RNF2          | Segurança         |
| RNF3          | Usabilidade       |

---

## 3. Tipos de Teste

Os seguintes tipos de teste serão aplicados ao sistema:

- **Teste de Interface de Usuário** – Avaliação da usabilidade e navegação.
- **Teste de Desempenho** – Medição da resposta do sistema (teste\_desempenho.py).
- **Teste de Carga** – Avaliação sob alto volume de requisições (teste\_carga.py).
- **Teste de Estresse** – Identificação do limite do sistema sob alta demanda (teste\_estresse.py).



### 3.1 Teste de Funcionalidade (farmácia.py, medicamento.py, principal.py)

**Objetivo:** Verificar se todas as funções do sistema operam corretamente.\
**Técnica:** (x) Manual (x) Automático\
**Estágio do Teste:** Integração (x) Sistema ( ) Unidade ( ) Aceitação ( )\
**Abordagem do Teste:** Caixa Branca (x) Caixa Preta (x)\
**Responsável:** Equipe de Desenvolvimento

### 3.2 Teste de Persistência de Dados

**Objetivo:** Garantir que os dados sejam armazenados corretamente e não sejam perdidos após desligamento do programa.\
**Técnica:** (x) Manual (x) Automático\
**Estágio do Teste:** Integração ( ) Sistema (x) Unidade ( ) Aceitação ( )\
**Abordagem do Teste:** Caixa Branca ( ) Caixa Preta (x)\
**Responsável:** Equipe de Testes

### 3.3 Teste de Integração dos Componentes

**Objetivo:** Testar a comunicação entre os módulos do sistema.\
**Técnica:** (x) Manual (x) Automático\
**Estágio do Teste:** Integração (x) Sistema ( ) Unidade ( ) Aceitação ( )\
**Abordagem do Teste:** Caixa Branca (x) Caixa Preta (x)\
**Responsável:** Equipe de Desenvolvimento

---

## 4. Recursos Necessários

### 4.1 Ambiente de Teste - Software e Hardware

- **Sistema Operacional:** Windows/Linux
- **Banco de Dados:** SQLite/MySQL
- **Linguagem:** Python
- **Ferramentas de Teste:** Pytest, Locust, Selenium (para interface, se houver)

### 4.2 Ferramentas de Teste

- **Pytest** – Para testes unitários e de integração.
- **Locust** – Para testes de carga e estresse.
- **Selenium** – Para automação da interface (caso necessário).

---

## 5. Cronograma

| Tipo de Teste | Duração | Data de Início | Data de Término |
| ------------- | ------- | -------------- | --------------- |
| Planejamento  | 2 dias  | 14/03/2025     | 16/03/2025      |
| Implementação | 3 dias  | 17/03/2025     | 20/03/2025      |
| Execução      | 4 dias  | 21/03/2025     | 25/03/2025      |
| Avaliação     | 2 dias  | 26/03/2025     | 28/03/2025      |

---

## 6. Critérios de Aceitação

O sistema será considerado aprovado se:

- **100% dos testes funcionais** forem concluídos com sucesso.
- **Os tempos de resposta** forem compatíveis com os requisitos de desempenho.
- **Os testes de carga e estresse** demonstrarem estabilidade.
- **Os dados persistirem corretamente** no banco de dados.
- **Não houver vulnerabilidades críticas** detectadas nos testes de segurança.

---

## 7. Conclusão

Este plano de teste foi elaborado para garantir a qualidade do **Sistema de Controle de Farmácia**. Todos os testes serão aplicados conforme o cronograma e os resultados serão analisados para garantir um sistema estável, seguro e eficiente.

**Acompanhamento e ajustes podem ser realizados conforme necessário durante o ciclo de desenvolvimento.**


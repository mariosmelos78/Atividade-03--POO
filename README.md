# Atividade de Métodos: Aula 03 — Programação Orientada a Objetos

Este repositório contém a resolução da **Atividade de Métodos (Aula 03)** da disciplina de Programação Orientada a Objetos do Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Maranguape.

O objetivo principal desta atividade é praticar a evolução de classes aplicando os conceitos de métodos, encapsulamento (`self`), retorno de valores booleanos para controle de fluxo, métodos especiais (`__str__`) e métodos de acesso (`getters` e `setters`).

## 🛠️ Requisitos Comuns Implementados

- **Uso do `self`:** Todos os atributos e métodos internos são acessados estritamente utilizando a referência do próprio objeto.
- **Encapsulamento de Retorno:** O método `__str__` apenas constrói e retorna a string correspondente, deixando a responsabilidade da impressão para o programa de teste.
- **Separação de Camadas:** Os métodos das classes não utilizam as funções `input()` nem `print()`. Toda a interação com o usuário e tomada de decisões acontecem exclusivamente nos programas de teste.
- **Controle de Ações:** Métodos que realizam modificações de estado retornam `True` em caso de sucesso ou `False` caso a ação seja inválida, permitindo mensagens dinâmicas no script de testes.
- **Padronização:** Identificadores escritos no padrão `snake_case` com verbos no infinitivo e prefixes padronizados para métodos de acesso (`get_` e `set_`).

---

## 📁 Estrutura do Projeto

Os arquivos foram organizados e nomeados seguindo estritamente as instruções fornecidas:

* `televisao.py`: Contém a classe `Televisao` com regras para controle de estado (ligada/desligada), canais (1 a 100) e volume (0 a 100).
* `testar_televisao.py`: Script de teste que cria múltiplas instâncias da TV, manipula seus estados de forma independente e valida os fluxos de erro.
* `aluno.py`: Contém a classe `Aluno` que gerencia o histórico de notas, controle de faltas e validação de critérios de aprovação escolar.
* `testar_aluno.py`: Script que processa uma lista de alunos, calcula as médias, avalia aprovações baseado em 40 aulas e encontra o destaque da turma.

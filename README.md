# Sistema Bancário Otimizado (Refatorado com Funções)

Este projeto é a evolução do sistema bancário simples, desenvolvido em Python, com foco na **organização do código** e na implementação de regras de negócio mais complexas. O projeto faz parte do bootcamp **NTT DATA - Engenharia de Dados com Python**, em parceria com a plataforma Dio.me.

## Destaques da Otimização
O código foi refatorado e organizado em funções (modularização) para melhorar a legibilidade, o reuso e a manutenção. Isso incluiu:
* **Funções Dedicadas:** Separação das responsabilidades de Saque, Depósito e Extrato.
* **Gestão de Entidades:** Funções específicas para `cadastrar_usuarios` e `criar_conta`.
* **Controle de Fluxo:** Utilização de `global` para manipulação de variáveis de estado (`saldo`, `extrato`).

---

## Funcionalidades
O sistema oferece um menu interativo e agora gerencia três tipos principais de operações:

### 🏦 Operações Bancárias
| Funcionalidade | Descrição | Regras de Negócio |
| :--- | :--- | :--- |
| **Depósito** | Adiciona valor ao saldo da conta. | Aceita apenas valores positivos (`valor_deposito > 0`). |
| **Saque** | Retira valor do saldo. | Limite por operação (R$ 500) e limite diário (5 saques). Verifica se o `saldo` é suficiente. |
| **Extrato** | Exibe o histórico. | Mostra todas as movimentações e o `Saldo Atual`. |

### 👤 Gestão de Usuários e Contas
* **Cadastro de Usuário:** Armazena `nome`, `data de nascimento`, **CPF (único)** e `endereço` (formatado). Utiliza uma função de filtragem para garantir que o **CPF não seja duplicado**.
* **Criação de Conta:** Cria uma conta corrente com **Agência Fixa** (`0001`) e **Número Sequencial**. A conta é vinculada a um usuário **já existente** no sistema, buscando-o pelo CPF.

---

## Tecnologias Utilizadas
* `Python`

---

## Instalação e Uso
Para rodar este projeto, você precisa ter o Python instalado na sua máquina.

1.  Salve o código completo em um arquivo com a extensão `.py`, por exemplo, `banco_otimizado.py`.
2.  Abra o terminal ou prompt de comando na pasta onde o arquivo foi salvo.
3.  Execute o comando abaixo:
    ```bash
    python banco_otimizado.py
    ```
4.  Para testar o sistema completo, chame as funções de cadastro no final do arquivo: `cadastrar_usuarios()`, seguido por `criar_conta()`.

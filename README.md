# 💰 Sistema Bancário em Python

**Professor:** Guilherme Arthur de Carvalho (@decarvalhogui)  
**Analista de Sistemas**  

---

## 📌 Descrição do Desafio
Este projeto é um **sistema bancário simples** desenvolvido em Python como parte de um exercício proposto pelo professor **Guilherme Arthur de Carvalho**.

O objetivo é implementar **três operações principais**:
1. **Depósito**
2. **Saque**
3. **Visualização de Extrato**

---

## Objetivo
O banco deseja modernizar suas operações e, para a **primeira versão (v1)**, foi solicitado um sistema capaz de:
- Receber depósitos de valores positivos.
- Permitir até 3 saques diários, com limite de **R$ 500,00** por saque.
- Mostrar um **extrato** listando todas as movimentações e o saldo final.

---

## Regras de Negócio

### Operação de Depósito
- Apenas **valores positivos** podem ser depositados.
- Todos os depósitos são armazenados e exibidos no **extrato**.
- Não há identificação de agência ou número de conta (apenas **1 usuário**).

### Operação de Saque
- Máximo de **3 saques por dia**.
- Limite de **R$ 500,00 por saque**.
- Se o saldo for insuficiente, o sistema deve informar a impossibilidade do saque.
- Todos os saques são registrados e exibidos no **extrato**.

### Operação de Extrato
- Lista todos os depósitos e saques realizados.
- Mostra o **saldo atual** no final.
- Caso não haja movimentações, exibe:

- Valores exibidos no formato:
 R$ xxx.xx
 Exemplo: 1500.45→R$1500.45


---

## Como Executar
1. Clone este repositório:
 ```bash
 git clone https://github.com/marciordalio/https://github.com/marciordalio/banco_python.git

 cd BANCO_PYTHON

 python sistema_bancario.py


 ```

## Como Executar


[1] Depositar<br>
[2] Sacar<br>
[3] Extrato<br>
[4] Ver Saldo<br>
[5] Sair<br>

Digite a opção desejada: 1<br>
Valor do depósito: R$ 200.00<br>

Digite a opção desejada: 3<br>
==== EXTRATO ====<br>
Depósito: R$ 200.00<br>
Saldo: R$ 200.00


## 📌 Observações

    Este projeto é apenas um exercício de prática.
    Não possui persistência em banco de dados (os dados são perdidos ao encerrar o programa).

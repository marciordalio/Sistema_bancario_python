menu = """
  Bem-vindo ao banco Python, seleciona uma opção: 
    1-Deposito
    2-Saque
    3-Extrato
    4-Ver saldo
    5-Sair
"""

saques_diarios = 3 
saldo = 0
extrato = ""
limite = 500
numeros_de_saque = 0
LIMITE_DE_SAQUE = 3
while True:
 
  opcao = int(input(f"{menu} Digite sua opção: "))


  if opcao == 1:
       deposito =  float(input(" \nQual valor deseja Depositar:" )) 
       if deposito>0:
         print(f" Foi depósitado R${deposito} ")
         extrato += f" Depósito de R$ {deposito:.2f}\n"
         saldo += deposito
       else:
         print(" O valor digitado é inválido , digite um valor VÀLIDO!")
         
         
  elif opcao == 2:
    saque = float(input(" \nQual valor deseja Sacar: "))
    
    
    

    excedeu_saldo = saque > saldo

    excedeu_limite = saque > limite

    excedeu_saque =  numeros_de_saque >= LIMITE_DE_SAQUE


    if excedeu_saldo  :
     print(" O Valor digitado é maior que seu saldo, digite um valor VÀLIDO!")

    elif excedeu_limite:
     print(" Digite um valor MENOR que R$500!")
    
    elif excedeu_saque: 
      print(" Numero máximo de saque diários atingido tente novamente amanhã!")
    
    elif saque >0: 
      print(f" Seu saque foi de {saque:.2f}")
      saldo -= saque 
      numeros_de_saque +=1
      extrato += f" Saque de R${saque}\n"

    else:
     print(" Operação inválida!")
   

  elif opcao == 3: 
  
     print("\n========EXTRATO==========")
     print(" Não foram realizadas movimentações!" if not extrato else extrato)
     print(extrato)
     print(f" R${saldo}")
     print("=========================")

  elif opcao == 4:
    print(f" \nSeu saldo atual é: {saldo}")

  elif opcao == 5:
    print(" Muito obrigado por usar nossos serviços!")
    break

  else:
    print(" Operação inválida, por favor seleciona uma operação VÀLIDA!")
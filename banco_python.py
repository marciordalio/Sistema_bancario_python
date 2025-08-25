

def menu():
 menu = int(input ( """
  ============= Bem-vindo ao banco Python, seleciona uma opção! =============
    1-Deposito
    2-Saque
    3-Extrato
    4-Ver saldo
    5-Sair
                    
    Digite sua opção:"""))
 
 return menu

def deposito(saldo, valor, extrato,/): # obrigando a passar sem parametro, não digitar parametro
       if valor>0:
         print(f" Foi depósitado R${valor} ")
         extrato += f" Depósito de R$ {valor:.2f}\n"
         saldo += valor
       else:
         print(" O valor digitado é inválido , digite um valor VÀLIDO!")
       return saldo, valor, extrato
                  
def saque(saldo, valor, extrato, limite, numeros_de_saque, limite_de_saque ):
 
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saque =  numeros_de_saque >= limite_de_saque


    if excedeu_saldo:
     print(" O Valor digitado é maior que seu saldo, digite um valor VÀLIDO!")

    elif excedeu_limite:
     print(" Digite um valor MENOR que R$500!")
    
    elif excedeu_saque: 
      print(" Numero máximo de saque diários atingido tente novamente amanhã!")
    
    elif valor >0: 
      print(f" Seu saque foi de {valor:.2f}")
      saldo -= valor 
      numeros_de_saque +=1
      extrato += f" Saque de R${valor}\n"

    else:
     print(" Operação inválida!")

    return saldo, extrato, valor, numeros_de_saque
   
def extrato(): 
  
     print("\n========EXTRATO==========")
     print(" Não foram realizadas movimentações!" if not extrato else extrato)
     print(extrato)
     print(f" R${saldo}")
     print("=========================")

def  saldo_atual():
    print(f" \nSeu saldo atual é: {saldo}")

def sair():
    print(" Muito obrigado por usar nossos serviços!")
   

def main():
 saques_diarios = 3 
 numeros_de_saque = 0
 saldo = 0
 extrato = ""
 limite = 500
 LIMITE_DE_SAQUE = 3

 #CHAMANDO FUNÇÔES

 while True:
   opcao = menu()
    
   if opcao == 1:
      valor = float(input("Qual valor deseja Depositar:")) 
      saldo, valor, extrato = deposito(saldo, valor, extrato)

   elif opcao ==2:
      valor = float(input("Qual o valor para o saque: "))

      saldo, extrato, valor, numeros_de_saque= saque(
         
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numeros_de_saque = numeros_de_saque,
        limite_de_saque = LIMITE_DE_SAQUE,
         

      )
      
main()
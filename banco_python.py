

def menu():
 menu = int(input ( """
  ============= Bem-vindo ao banco Python, seleciona uma opção! =============
    1-Deposito
    2-Saque
    3-Extrato
    4-Ver saldo
    5-Novo usuário             
    6-Criar conta
                    
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
   
def extrato_func(saldo, / ,*,extrato): 
     
  
     print("\n========EXTRATO==========")
     print(" Não foram realizadas movimentações!" if not extrato else extrato)
     print(extrato)
     print(f" R${saldo}")
     print("=========================")

def saldo_atual(saldo):
    
    print("==============================")
    print(f" \nSeu saldo atual é: {saldo}")
    print("==============================")

def novo_usuario(lista_de_usuarios):#lista de usuarios vai armazenar os usuarios em uma lista
   cpf = input("informe seu CPF(somente numeros)")


   if filtra_usuario(cpf, lista_de_usuarios):
      print("Usuário já existe!")
      return
   
   else:
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço: ")
    lista_de_usuarios.append({"nome": nome,"data_de_nascimento":data_de_nascimento, "endereco":endereco, "cpf":cpf })
    print("Usuário criado com sucesso, pode criar uma CONTA!")

def filtra_usuario(cpf, lista_de_usuarios):
   for usuarios in lista_de_usuarios:
      if usuarios["cpf"] == cpf:
         return True
   return False
  
def criar_conta(agencia, numero_conta, lista_de_usuarios):

   cpf = input("informe seu CPF(somente numeros: )")
      
   usuario = filtra_usuario(cpf, lista_de_usuarios)
      
   if usuario:
    print("\n=== Conta criada com sucesso! ===")
    numero_conta = input("Digite o número da conta: ")   
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
   
   else:
        print("\nUsuário não encontrado, por favor crie um usuário antes de criar uma conta!")
        return None


   

def sair():
    print(" Muito obrigado por usar nossos serviços!")
   
def main():
 AGENCIA = "0001"
 saques_diarios = 3 
 numeros_de_saque = 0
 saldo = 0
 extrato = ""
 limite = 500
 LIMITE_DE_SAQUE = 3
 lista_de_usuarios= []
 contas = []

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
   elif opcao == 3:
      extrato_func(saldo , extrato = extrato)


   elif opcao ==4:
      saldo_atual(saldo)

   elif opcao == 5: 
      novo_usuario(lista_de_usuarios )
      
   elif opcao == 6:
      numero_conta = ""  # Defina um valor inicial para numero_conta
      nova_conta= criar_conta(AGENCIA, numero_conta, lista_de_usuarios)
      if nova_conta:
        contas.append(nova_conta)
   
   elif opcao == 7:
      sair()
      break
   else:
      print("Opção inválida!")
         
      
main()
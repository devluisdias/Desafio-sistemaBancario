def menu():
  menu_opcoes = """
  -------------
  [d] Depositar
  [s] Sacar
  [m] Saldo
  [e] Extrato
  [n] Novo Usuário
  [q] Sair 
  -------------
  => """
  return input(menu_opcoes).lower()

def deposito(valor, saldo, extrato, /):              
  if valor > 0:
      saldo += valor
      extrato += f"DEPÓSITO R$ {valor:.2f}\n"
      print(f"Você depositou o valor de R$ {valor:.2f} em sua conta bancária.")
  else:
      print("Tente novamente com um valor válido!")
  return saldo, extrato

def saque(*, valor_saque, saldo, extrato, quantidade_saques, limite_saque):
  if valor_saque <= saldo and quantidade_saques < LIMITE_SAQUE:
    saldo -= valor_saque
    quantidade_saques += 1
    print(f"Você sacou o valor de R$ {valor_saque:.2f} da sua conta bancária!")  
    extrato += f"SAQUE R$ -{valor_saque:.2f}\n"

  elif valor_saque > limite:
    print("O valor excede o limite de saque por operação. Tente novamente com um valor válido!\n")

  elif quantidade_saques == limite_saque:
    print("Numero máximo de saque diário excedido!")
    
  elif valor_saque > saldo:
    print("O valor excede o saldo presente na conta bancária!")

  else:
      print("Valor inválido! Tente novamente.")
      
  return saldo, extrato

def visualizar_saldo(saldo):
  print("Você escolheu a opção SALDO!")
  print(f"Você possui R$ {saldo} em conta!")

def visualizar_extrato(saldo,/ , *, extrato):
  print("-"*15,"EXTRATO","-"*15)
  if extrato.strip() == '':
    print("Não houveram movimentações!")
    print(f"\nSaldo: R$ {saldo:.2f}")
  else:
    print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-"*37)

def criar_usuario(clientes):
  cpf = input("Digite o seu CPF: ")
  usuario = filtrar_clientes(cpf, clientes)
  if usuario:
    print('Este usuário já existe)')

  nome = input("Digite o seu nome: ")
  data_nascimento = input("Digite a sua data de nascimento (dd-mm-aaaa): ")
  endereco = input("Digite o seu endereço: ")
  clientes.append({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco})
  print('Usuário criado com sucesso!')

def filtrar_clientes(cpf, clientes):
  filtragem = [usuario for usuario in clientes if usuario["cpf"] == cpf]
  return filtragem[0] if filtragem  else None

def criar_conta(AGENCIA, numero_conta, clientes):
  cpf = input('Digite o seu cpf: ')
  usuario = filtrar_clientes(cpf, clientes)
  
  if usuario:
    print("\nConta criada com sucesso!")
    return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
  


    

saldo = 0; limite = 500; extrato = ""; clientes = []; contas = []
quantidade_saques = 0; LIMITE_SAQUE = 3; AGENCIA = "0001"

while True: 
  escolha = menu()

  if escolha == 'd':
    print("Você escolheu a opção de DEPÓSITO!")
    valor = float(input("Digite a quantia que você deseja depositar: "))  
    saldo, extrato = deposito(valor, saldo, extrato)   
  
  elif escolha == 's':
    print("Você escolheu a opção de SAQUE!")
    valor_saque = float(input("Digite a quantia que você deseja sacar: "))
    saldo, extrato = saque(
      valor_saque = valor_saque, 
      saldo = saldo, 
      extrato = extrato, 
      quantidade_saques = quantidade_saques, 
      limite_saque = LIMITE_SAQUE)

  elif escolha == "m":
    visualizar_saldo(saldo)

  elif escolha == "e":
    visualizar_extrato(saldo, extrato=extrato)
  
  elif escolha == "n":
    criar_usuario(clientes)
  
  elif escolha == "c":
    numero_conta = len(contas) + 1
    conta = criar_conta(AGENCIA, numero_conta, clientes)
    if conta:
      contas.append(conta)
  
  elif escolha == "q":
      print("\n PROGRAMA FINALIZADO! ")
      break
  
  else:
    print("Operação inválida! Tente novamente.")
    break
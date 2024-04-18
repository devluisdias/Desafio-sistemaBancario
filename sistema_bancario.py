menu = """
-------------
[d] Depositar
[s] Sacar
[m] Saldo
[e] Extrato
[q] Sair 
-------------
=> """

saldo = 0; limite = 500; extrato = ""
quantidade_saques = 0; LIMITE_SAQUE = 3

while True: 
  escolha = input(menu).lower()

  if escolha == 'd':
    print("Você escolheu a opção de DEPÓSITO!")
    valor = float(input("Digite a quantia que você deseja depositar: "))
    
    if valor > 0:
      saldo += valor
      print(f"Você depositou o valor de R$ {valor:.2f} em sua conta bancária.")
      extrato += f"DEPÓSITO R$ {valor:.2f}\n"
      continue
    else:
      print("Tente novamente com um valor válido!")
      continue
  
  elif escolha == 's':
    print("Você escolheu a opção de SAQUE!")
    saque = float(input("Digite a quantia que você deseja sacar: "))

    if saque <= saldo and quantidade_saques < LIMITE_SAQUE:
      saldo -= saque
      quantidade_saques += 1
      print(f"Você sacou o valor de R$ {saque:.2f} da sua conta bancária!")  
      extrato += f"SAQUE R$ -{saque:.2f}\n"
      continue

    elif saque > limite:
      print("O valor excede o limite de saque por operação. Tente novamente com um valor válido!\n")
      continue

    elif quantidade_saques == LIMITE_SAQUE:
      print("Numero máximo de saque diário excedido!")
      continue
    
    elif saque > saldo:
      print("O valor excede o saldo presente na conta bancária!")
      continue
    
    else:
      print("Valor inválido! Tente novamente.")
      continue
  
  elif escolha == "m":
    print("Você escolheu a opção SALDO!")
    print(f"Você possui R$ {saldo} em conta!")
    continue


  elif escolha == "e":
    print("-"*15,"EXTRATO","-"*15)
    if extrato.strip() == '':
      print("Não houveram movimentações!")
      print(f"\nSaldo: R$ {saldo:.2f}")
      continue
    else:
      print(extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("-"*37)
      continue
  
  elif escolha == "q":
      print("Programa finalizado!")
      break
  
  else:
    print("Operação inválida! Tente novamente.")
    break
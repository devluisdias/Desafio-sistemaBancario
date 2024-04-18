from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
  def __init__(self, endereco):
    self._endereco = endereco
    self._contas = []
  
  def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)
  
  def adicionar_conta(self, conta):
    self.contas.append(conta)

class PessoaFisica(Cliente):
  def __init__(self, nome, endereco, data_nascimento, cpf):
    super().__init__(endereco)
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf = cpf

class Conta:
  def __init__(self, numero, Cliente):
    self._saldo = 0
    self._numero = numero
    self._agencia = "0001"
    self._cliente = Cliente
    self._historico = Historico()

  @classmethod
  def nova_conta(cls, cliente, numero):
    return cls(cliente, numero)
  
  @property
  def saldo(self):
    return self._saldo
  
  @property
  def numero(self):
    return self._numero
  
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def cliente(self):
    return self._cliente
  
  @property
  def historico(self):
    return self._historico
  
  def sacar(self, valor):
    saldo = self.saldo
    saldo_excedido = valor > saldo

    if saldo_excedido:
      print("\n Operação não realizada, pois o valor excede o saldo da conta.")
    
    elif valor > 0:
      self._saldo -= valor
      print("\n Saque realizado com sucesso!")

    else: print("\n Operação não realizada, pois o valor é inválido.")

    return False
  
  def depositar(self, valor):              
    if valor > 0:
        self._saldo += valor
        print(f"Você depositou o valor de R$ {valor:.2f} em sua conta bancária.")
    else:
        print("Tente novamente com um valor válido!")
        return False
    
    return True

class ContaCorrente(Conta):
  def __init__(self, numero, cliente, limite=500, limite_saques=3):
    super().__init__(numero, cliente)
    self.limite = limite
    self.limite_saques = limite_saques

  def sacar(self, valor):
    numero_saques = len(
      [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
    )

    limite_excedido = valor > self.limite
    saques_excedido = numero_saques >= self.limite_saques

    if limite_excedido:
      print("Operação não realizada, pois o valor do saque excede o limite.")

    elif saques_excedido:
      print("Operação não realizada, pois o número máximo de saques diários foi alcançado.")

    else: 
      return super().sacar(valor)
    
    return False
  
  def __str__(self):
    return f"""\
        Agência: {self.agencia}
        N° da conta: {self.numero}
        Titular: {self.cliente.nome}
  """
   
class Transacao(ABC):
  @property
  @abstractproperty
  def valor(self):
    pass

  @abstractclassmethod
  def registrar(self,conta):
    pass
       
class Saque(Transacao):
  def __init__(self, valor):
    self._valor = valor
  
  @property
  def valor(self):
    return self._valor
  
  def registrar(self, conta):
    transacao_completa = conta.sacar(self.valor)

    if transacao_completa:
      conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor
  
  @property
  def valor(self):
    return self._valor
  
  def registrar(self, conta):
    transacao_completa = conta.depositar(self.valor)

    if transacao_completa:
      conta.historico.adicionar_transacao(self)

class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes
  
  def adicionar_transacao(self, transacao):
    self._transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
      }
    )

    
    

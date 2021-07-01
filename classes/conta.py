from abc import ABC, abstractmethod


class Conta(ABC):
    from typing import Union
    def __init__(self, agencia: str, conta: str, saldo: float = 0):
        """
        Vai inicializar a classe abstrata de conta
        :param agencia: numero da agencia do banco
        :param conta:  numero da conta do banco
        :param saldo: saldo da conta, definido como 0, caso não seja alterado
        """

        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self.libera = False

    @property
    def agencia(self):
        """getter para atributo _agencia que está encabsulado"""
        return self._agencia

    @property
    def conta(self):
        """getter para atributo _conta que está encabsulado"""
        return self._conta

    @property
    def saldo(self):
        """getter para atributo _saldo que está encabsulado"""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """setter para alterar o valor de _saldo que está encabsulado"""
        if isinstance(valor, int):
            self._saldo = valor
        elif isinstance(valor, float):
            self._saldo = valor
        else:
            return print("não é possivel adicionar esse tipo de valor a conta")

    def depositar(self, valor=0):
        """vai depositar um valor dentro da conta"""
        try:
            self.saldo += valor
        except TypeError as erro:
            print("O valor deve ser númerico")

    def mostra_conta(self):
        """vai mostrar o valores da conta de forma formatada"""
        print(f"Conta: {self.conta}\nAgência: {self.agencia}\nSaldo: {self.saldo}")

    @abstractmethod
    def sacar(self):
        """metodo de sacar que vai ser reescrito nas classes ContaCorrente e ContaPoupanca"""
        pass


class CP(Conta):
    """Classe que herda de conta que representa uma conta poupança
    -tem uma função que saca, que se diferencia da conta corrente, sendo que não pode ficar negativa
    """

    def sacar(self, valor_de_saque=0):
        """
        função para sacar, esse metodo está por padrão bloqueado, sendo que o self.libera será True,
        de acordo com a autenticação feito na classe Banco
        :param valor_de_saque: valor que vai ser retirado da conta
        :return: None
        """
        LIMITE = 0
        if self.libera:
            try:
                if LIMITE + self.saldo < valor_de_saque:
                    print("saldo insuficiente")
                else:
                    self.saldo -= valor_de_saque
            except TypeError:
                print("digite um valor inteiro ou de float para conseguir realizar o saque")
        else:
            print("A opção de saque está bloqueada")


class CC(Conta):
    """
    Classe que herda da classe Conta e e tem uma função que a diferencia para representar uma conta corrente
    """

    def __init__(self, agencia: str, conta: str, saldo: float = 0, cheque_especial = 100):
        super().__init__(agencia, conta, saldo)
        self.cheque_especial = cheque_especial

    def sacar(self, valor_de_saque):
        """
        função para retirar valor da conta, é diferente da classe conta poupança, pois tem o cheque especial
        Esté metodo está bloqueado e será liberado de acordo com a autenticação feita na classe Banco
        :param valor_de_saque: valor a ser retirado da conta
        :param cheque_especial: valor de limite a ficar negativo na conta
        :return:  None
        """

        if self.libera:
            try:
                if self.cheque_especial + self.saldo < valor_de_saque:
                    print("saldo insuficiente...")
                else:
                    self.saldo -= valor_de_saque
            except TypeError:
                print("digite um valor inteiro ou de float para conseguir realizar o saque")
        else:
            print("A opção de saque está bloqueada")
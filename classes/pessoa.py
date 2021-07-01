from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        """
    Essa classe, vai inicializar nosso objeto base, que representa uma pessoa
    tendo nome e idade
        """
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        """getter para o atributo que está 'encabsulado'"""
        return self._nome

    @nome.setter
    def nome(self, valor):
        "setter para alterar valor de atributo _nome"
        self._nome = valor


    @property
    def idade(self):
        """getter para o atributo que está 'encabsulado'"""
        return self._idade

    @idade.setter
    def idade(self, valor):
        "setter para alterar o valor do atributo _idade"
        self._idade = valor


    @abstractmethod
    def ativar_cp(self):
        pass

class Cliente(Pessoa):
    from classes.conta import CC
    def __init__(self, nome, idade,agencia: str, conta:str, saldo = 0):
        super().__init__(nome, idade)
        from classes.conta import CC
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.cc = CC(self.conta, self.agencia, self.saldo)
        self._cp = None

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, valor):
        self._cp = valor


    def ativar_cp(self):
        """Esse metodo vai liberar a opção de conta poupança para um cliente"""
        from classes.conta import CP
        self.cp = CP(self.conta, self.agencia, self.saldo)




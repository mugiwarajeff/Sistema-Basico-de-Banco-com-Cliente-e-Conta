from classes.conta import *
from classes.pessoa import *

class Banco():
    def __init__(self, nome: str):
        """
        Método de inicialização da classe banco, que autenticará o saque do cliente, o banco terá um nome, e também seus bancos de contas,clientes e agencias
        :param nome: nome da do banco
        """
        self.nome = nome
        self.banco_de_conta = ["50791-1"]
        self.banco_de_clientes = ["Jeff"]
        self.banco_de_agencias = ["3548"]

    def login_na_conta(self, cliente: object):
        """
        Essa função irá fazer o login do cliente na conta do banco, permitindo que a opção de saque seja liberada
        :param cliente: é um objeto instanciado da classe Cliente que desejará ter seu saque permitido
        :return: None
        """
        if cliente.conta in self.banco_de_conta and cliente.agencia in self.banco_de_agencias and cliente.nome in self.banco_de_clientes:
            cliente.cc.libera = True
            print(f"cliente {cliente.nome} foi logado com sucesso!")
        else:
            print("Algo deu errado, cheque as informações e tente novament")




"""
Exercicio com abstração, Herança, Encabsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco.
A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta.
contas corrente tem um limite extra. Banco tem clientes e contas


Dicas:

Criar classe Cliente que herda da classe Pessoa(herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdem de conta
    ContaCorrente deve ter um limite extra
    Contas tem agência, numero da conta e saldo
    Contas devem ter método para depósito
    conta (super classe) deve ter o método sacar abstrato (abstração e polimorgismo - as subclasses que
    implementam o método sacar)
Criar classe Banco para Agregar classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguintes maneiras:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
só será possivel sacar se passar na autenticação do banco (descrita acima)


"""
from classes.pessoa import *
from classes.conta import *
from classes.banco import Banco
cliente1 = Cliente("Jeff", 19, "3548", "50791-1")
b1 = Banco("Bradesco")
b1.login_na_conta(cliente1)
cliente1.cc.sacar(50)
cliente1.cc.mostra_conta()


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def obter_saldo(self):
        return self.saldo

class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.contas= {}

    def AbrirConta(self, titular,saldo_inicial=0):
        conta = ContaBancaria(titular,saldo_inicial)
        self.contas[conta.titular]=conta

    def obter_saldo(self, titular):
        if titular in self.contas:
            return self.contas[titular].obter_saldo()
        else:
            print("Titular não encontrado")

    def depositar(self,titular,valor):
        if titular in self.contas:
            self.contas[titular].depositar(valor)
        else:
            print("Titular não encontrado.")

    def sacar(self,titular, valor):
        if titular in self.contas:
            self.contas[titular].sacar(valor)
        else:
            print("Titular não encontrado.")

    def exibir_contas(self):
        print(f"Contas do Banco {self.nome}:")
        for titular, conta in self.contas.items():
            print(f"Titular: {titular} | Saldo: R${conta.obter_saldo()}")

banco=Banco("PyBank")
banco.AbrirConta("Leo",100000)

banco.depositar("Leo",5000)
banco.sacar("Leo",2000)

saldo_leo = banco.obter_saldo("Leo")

print(f"Saldo de Leonardo:R${saldo_leo}")

banco.exibir_contas()

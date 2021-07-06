class Adress():
    def __init__(self):
        self.cep = int()
        self.numero = int()
        self.rua = str()
        self.bairro = str()
        self.cidade = str()
        self.estado = str()

    def Show(self):
        print('Rua:', self.rua)
        print('Número:', self.numero)
        print('Bairro:', self.bairro)
        print('Cidade:', self.cidade)
        print('Estado:', self.estado)
        print('CEP:', self.cep)


class Syndicate():
    def __init__(self, name):
        self.name = name

    def Show(self):
        print('Nome:', self.name)


class Historico():
    def __init__(self):
        self.ponto = {}
        self.venda = {}
        self.taxa = {}


class Person():
    def __init__(self, name, type, paymethod, syndicate = None):
        self.name = name
        self.type = type
        self.paymethod = paymethod
        self.adress = Adress()
        self.syndicate = Syndicate(syndicate) if syndicate is not None else None
        self.historico = Historico()

    def SetAdress(self, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if cep:
            self.adress.cep = cep
        if numero:
            self.adress.numero = numero
        if rua:
            self.adress.rua = rua
        if bairro:
            self.adress.bairro = bairro
        if cidade:
            self.adress.cidade = cidade
        if estado:
            self.adress.estado = estado

    def ShowInfo(self):
        if self.type == 1:
            type = "Horista"
        if self.type == 2:
            type = "Assalariado"
        if self.type == 3:
            type = "Comissionado"
        if self.paymethod == 1:
            paymethod = "Cheque pelos Correios"
        if self.paymethod == 2:
            paymethod = "Cheque em mãos"
        if self.paymethod == 3:
            paymethod = "Depósito bancário"
        print('Nome:', self.name)
        print('Tipo:', type)
        print('Método de pagamento:', paymethod)
        if self.syndicate: 
            print('Pertence ao sindicato:')
            self.syndicate.Show()
        print('ENDEREÇO:')
        self.adress.Show()
        


var = Person('mickael', 1, 2)
var.SetAdress(57038485, 7, 'B', 'Cruz das Almas', 'Maceió', 'Alagoas')
var.ShowInfo()
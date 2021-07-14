import time


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


class Sale():
    def __init__(self, value):
        self.time = time.asctime()
        self.value = value

class Historico():
    def __init__(self):
        self.pontos = list()
        self.vendas = list()
        self.taxas = list()


class Person():
    def __init__(self):
        self.name = str()
        self.cpf = str()
        self.paymethod = int()
        self.adress = Adress()
        self.syndicate = bool()
        self.historico = Historico()

    def SetAdress(self, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if cep: self.adress.cep = cep
        if numero: self.adress.numero = numero
        if rua: self.adress.rua = rua
        if bairro: self.adress.bairro = bairro
        if cidade: self.adress.cidade = cidade
        if estado: self.adress.estado = estado

    def SetInfo(self, name = None, cpf = None, type = None, paymethod = None, syndicate = None):
        if name: self.name = name
        if type: self.type = type
        if cpf: self.cpf = cpf
        if paymethod: self.paymethod = paymethod
        if syndicate: self.syndicate = syndicate

    def ShowInfo(self):
        if self.type == 1: type = "Horista"
        if self.type == 2: type = "Assalariado"
        if self.type == 3: type = "Comissionado"
        if self.paymethod == 1: paymethod = "Cheque pelos Correios"
        if self.paymethod == 2: paymethod = "Cheque em mãos"
        if self.paymethod == 3: paymethod = "Depósito bancário"
        print('Nome:', self.name)
        print('CPF:', self.cpf)
        print('Tipo:', type)
        print('Método de pagamento:', paymethod)
        if self.syndicate: print('Pertence ao sindicato')
        else: print('Não pertence ao sindicato')
        print('ENDEREÇO:')
        self.adress.Show()


class Hourly(Person):
    def __init__(self):
        super().__init__()
        self.type = 1
        self.pontos = list()

    def regPonto(self, date):
        self.pontos.append(date)
        print(self.pontos)


class Salaried(Person):
    def __init__(self):
        super().__init__()
        self.type = 2


class Commissioned(Person):
    def __init__(self):
        super().__init__()
        self.type = 3
        self.sales = list()

    def regSale(self, sale):
        self.sales.append(sale)
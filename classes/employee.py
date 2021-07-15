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
    def __init__(self, taxa, id):
        self.taxa = taxa
        self.id = id


class Person():
    def __init__(self):
        self.name = str()
        self.cpf = str()
        self.paymethod = int()
        self.adress = Adress()
        self.syndicate = bool()
        self.type = int()

    def SetAdress(self, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if cep: self.adress.cep = cep
        if numero: self.adress.numero = numero
        if rua: self.adress.rua = rua
        if bairro: self.adress.bairro = bairro
        if cidade: self.adress.cidade = cidade
        if estado: self.adress.estado = estado

    def SetInfo(self, name = None, cpf = None, paymethod = None, syndicate = None):
        if name: self.name = name
        if cpf: self.cpf = cpf
        if paymethod: self.paymethod = paymethod
        if syndicate: self.syndicate = syndicate
    
    def getInfo(self, name = False, cpf = False, paymethod = False, type = False, syndicate = False, all = False):
        if all:
            info = {}
            info['name'] =  self.name
            info['cpf'] = self.cpf
            info['paymethod'] = self.paymethod
            info['syndicate'] = self.syndicate
            info['type'] = self.type
            return info
        else:
            if name: return self.name
            if cpf: return self.cpf
            if paymethod: return self.paymethod
            if syndicate: return self.syndicate
            if type: return self.type

    def getAdress(self, cep = False, rua = False, numero = False, bairro = False, cidade = False, estado = False, all = False):
        if all:
            adress = {}
            adress['cep'] = self.adress.cep
            adress['rua'] = self.adress.rua
            adress['numero'] = self.adress.numero
            adress['bairro'] = self.adress.bairro
            adress['cidade'] = self.adress.cidade
            adress['estado'] = self.adress.estado
            return adress
        else:
            if cep: return self.adress.cep
            if rua: return self.adress.rua
            if numero: return self.adress.numero
            if bairro: return self.adress.bairro
            if cidade: return self.adress.cidade
            if estado: return self.adress.estado


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
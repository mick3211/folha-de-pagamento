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
    
    def getInfo(self, name = True, cpf = True, paymethod = True, type = True, syndicate = True):
        info = {}
        if name: info['name'] =  self.name
        if cpf: info['cpf'] = self.cpf
        if paymethod: info['paymethod'] = self.paymethod
        if syndicate: info['syndicate'] = self.syndicate
        if type: info['type'] = self.type
        return info

    def getAdress(self, cep = True, rua = True, numero = True, bairro = True, cidade = True, estado = True):
        adress = {}
        if cep: adress['cep'] = self.adress.cep
        if rua: adress['rua'] = self.adress.rua
        if numero: adress['numero'] = self.adress.numero
        if bairro: adress['bairro'] = self.adress.bairro
        if cidade: adress['cidade'] = self.adress.cidade
        if estado: adress['estado'] = self.adress.estado
        return adress


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
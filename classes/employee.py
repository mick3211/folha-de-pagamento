class Adress():
    def __init__(self):
        self.cep = str()
        self.numero = int()
        self.rua = str()
        self.bairro = str()
        self.cidade = str()
        self.estado = str()


class Syndicate():
    def __init__(self, taxa, id):
        self.syn_tax = taxa
        self.serv_tax = list()
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

    def SetInfo(self, name = None, cpf = None, paymethod = None, syndicate = None, taxa = None, agenda = None):
        if name: self.name = name
        if cpf: self.cpf = cpf
        if paymethod: self.paymethod = paymethod
        if syndicate == False: self.syndicate = False
        else: self.syndicate = Syndicate(taxa, self.cpf)
        if agenda: self.agenda = agenda

    
    def getInfo(self, name = True, cpf = True, paymethod = True, type = True, syndicate = True):
        info = {}
        if name: info['name'] =  self.name
        if cpf: info['cpf'] = self.cpf
        if paymethod: info['paymethod'] = self.paymethod
        if syndicate:
            if self.syndicate != False:
                info['syndicate'] = True
                info['taxa'] = self.syndicate.syn_tax
            else: info['syndicate'] = False
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
        self.hisPontos = list()
        self.agenda = (2, 1, 6)

    def regPonto(self, date):
        self.hisPontos.append(date)


class Salaried(Person):
    def __init__(self):
        super().__init__()
        self.type = 2
        self.agenda = (1, 30)


class Commissioned(Person):
    def __init__(self):
        super().__init__()
        self.type = 3
        self.hisVendas = list()
        self.agenda = (2, 2, 6)

    def regSale(self, sale):
        self.hisVendas.append(sale)
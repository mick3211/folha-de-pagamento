class Adress():
    def __init__(self):
        self.cep = int()
        self.numero = str()
        self.rua = str()
        self.bairro = str()
        self.cidade = str()
        self.estado = str()
    
    def SetCep(self, cep):
        self.cep = cep

    def SetRua(self, rua):
        self.rua = rua
    
    def SetNumero(self, numero):
        self.numero = numero

    def SetBairro(self, bairro):
        self.bairro = bairro

    def SetCidade(self, cidade):
        self.cidade = cidade

    def SetEstado(self, estado):
        self.estado = estado


class Person():
    def __init__(self, name, type, paymethod, syndicate):
        self.name = name
        self.adress = Adress()
        self.type = type
        self.paymethod = paymethod
        self.syndicate = syndicate

    def SetAdress(self, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if cep:
            self.adress.SetCep(cep)
            print('cep setado')
        if numero != None:
            self.adress.SetNumero(numero)
        if rua != None:
            self.adress.SetRua(rua)
        if bairro != None:
            self.adress.SetBairro(bairro)
        if cidade != None:
            self.adress.SetCidade(cidade)
        if estado != None:
            self.adress.SetEstado(estado)
        

var = Person('mickael', 1, 2, 3)
var.SetAdress(numero = 8)
print(var)
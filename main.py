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
        self.pontos = {}
        self.vendas = {}
        self.taxas = {}


class Person():
    def __init__(self, name, type, paymethod, syndicate = None):
        self.name = name
        self.type = type
        self.paymethod = paymethod
        self.adress = Adress()
        self.syndicate = Syndicate(syndicate) if syndicate is not None else None
        self.historico = Historico()

    def SetAdress(self, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if cep: self.adress.cep = cep
        if numero: self.adress.numero = numero
        if rua: self.adress.rua = rua
        if bairro: self.adress.bairro = bairro
        if cidade: self.adress.cidade = cidade
        if estado: self.adress.estado = estado

    def SetInfo(self, name = None, type = None, paymethod = None):
        if name: self.name = name
        if type: self.type = type
        if paymethod: self.paymethod = paymethod

    def ShowInfo(self):
        if self.type == 1: type = "Horista"
        if self.type == 2: type = "Assalariado"
        if self.type == 3: type = "Comissionado"
        if self.paymethod == 1: paymethod = "Cheque pelos Correios"
        if self.paymethod == 2: paymethod = "Cheque em mãos"
        if self.paymethod == 3: paymethod = "Depósito bancário"
        print('Nome:', self.name)
        print('Tipo:', type)
        print('Método de pagamento:', paymethod)
        if self.syndicate: 
            print('Pertence ao sindicato:')
            self.syndicate.Show()
        print('ENDEREÇO:')
        self.adress.Show()


class Sys():
    EmployeeList = list()
    EmployeeNum = 0
    CurrentEmployee = None

    def ShowEmployees():
        for i, employee in enumerate(Sys.EmployeeList):
            print(f'{i}.', employee.name)

    def SetCurrent(id = None):
        if id == None:
            Sys.ShowEmployees()
            id = int(input('Selecione o funcionário: '))
        Sys.CurrentEmployee = Sys.EmployeeList[id]  
        return Sys.CurrentEmployee

    def AddEmployee(name, type, paymethod, adress, syndicate = None):
        new_employee = Person(name, type, paymethod, syndicate)
        new_employee.SetAdress(*adress)
        Sys.EmployeeList.append(new_employee)
        Sys.SetCurrent(Sys.EmployeeNum)
        Sys.EmployeeNum += 1

    def RemoveEmployee(id = None):
        if id == None: del(Sys.CurrentEmployee)
        else: del(Sys.EmployeeList[id])


class menu():
    def AddEmployee():
        name = input('Digite o nome do novo empregado: ')
        type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: '))
        paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: '))
        adress = list()
        print('Endereço:')
        adress.append(int(input('Digite o CEP: ')))
        adress.append(int(input('Digite o Número da casa: ')))
        adress.append(input('Digite a rua: '))
        adress.append(input('Digite o bairro: '))
        adress.append(input('Digite a cidade: '))
        adress.append(input('Digite o estado: '))

        Sys.AddEmployee(name, type, paymethod, adress)
        print('Novo empregado adicionado:')
        Sys.CurrentEmployee.ShowInfo()


    def RemoveEmployee():
        Sys.SetCurrent()
        Sys.RemoveEmployee()


    def EditEmployee():
        print('--------------')
        current = Sys.SetCurrent()
        print('EMPREGADO SELECIONADO:')
        current.ShowInfo()

        def editAdress():
            while True:
                print('--SELLECIONE UMA OPÇÃO--')
                print('1.Altera CEP\n2.Alterar Rua\n3.Alterar número\n4.Alterar bairro\n5.Alterar cidade\n6.Alterar Estado\n7.Voltar')
                op = int(input())
                if op == 1: current.SetAdress(cep = int(input('Novo CEP: ')))
                if op == 2: current.SetAdress(rua = input('Nova rua: '))
                if op == 3: current.SetAdress(numero = input('Novo número: '))
                if op == 4: current.SetAdress(bairro = input('Novo bairro: '))
                if op == 5: current.SetAdress(cidade = input('Nova cidade: '))
                if op == 6: current.SetAdress(estado = input('Novo Estado: '))
                if op == 7: break

        while True:
            print('--SELLECIONE UMA OPÇÃO--')
            print('1.Editar nome\n2.Alterar tipo\n3.Alterar método de pagamento\n4.Editar endereço\n5.Sair')
            option = int(input())
            if option == 1:
                current.SetInfo(name = input('Digite o novo nome: '))
            if option == 2:
                current.SetInfo(type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: ')))
            if option == 3:
                current.SetInfo(paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: ')))
            if option == 4: editAdress()
            if option == 5: break
        
        print('--EMPREGADO EDITADO--')
        current.ShowInfo()


while True:
    print('--SELLECIONE UMA OPÇÃO--')
    print('1.Adicionar empregado\n2.Remover empregado\n3.Editar empregado\n4.Listar empregados\n5.SAIR')
    option = int(input())
    if option == 1: menu.AddEmployee()
    if option == 2: menu.RemoveEmployee()
    if option == 3: menu.EditEmployee()
    if option == 4: Sys.ShowEmployees()
    if option == 5: break

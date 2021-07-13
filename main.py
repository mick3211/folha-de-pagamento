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


class Sys():
    EmployeeList = {}
    EmployeeNum = 0
    CurrentEmployee = None

    def ShowEmployees():
        if Sys.EmployeeNum > 0:
            for i, employee in Sys.EmployeeList.items:
                print(f'{i}:', employee.name)
            return True
        else:
            print('SEM FUNCIONÁRIOS CADASTRADOS')
            return False

    def SetCurrent(id):
        if id in Sys.EmployeeList.keys():
            Sys.CurrentEmployee = Sys.EmployeeList[id]  
            return Sys.CurrentEmployee
        else: return False

    def AddEmployee(name, cpf, type, paymethod, adress, syndicate = None):
        if type == 1: new_employee = Hourly()
        if type == 2: new_employee = Salaried()
        if type == 3: new_employee = Commissioned()
        new_employee.SetInfo(name, cpf, None, paymethod, syndicate)
        new_employee.SetAdress(*adress)
        Sys.EmployeeList[cpf] = new_employee
        Sys.EmployeeNum += 1
        Sys.SetCurrent(cpf)

    def RemoveEmployee(id = None):
        if id == None: del(Sys.CurrentEmployee)
        else: del(Sys.EmployeeList[id])


class menu():
    def AddEmployee():
        name = input('Digite o nome do novo empregado: ')
        cpf = input('Insira o CPF: ')
        type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: '))
        paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: '))
        adress = list()
        syndicate = True if input('Faz parte do sindicato? [s/n]: ') in 'Ss' else False
        print('Endereço:')
        adress.append(int(input('Digite o CEP: ')))
        adress.append(int(input('Digite o Número da casa: ')))
        adress.append(input('Digite a rua: '))
        adress.append(input('Digite o bairro: '))
        adress.append(input('Digite a cidade: '))
        adress.append(input('Digite o estado: '))

        Sys.AddEmployee(name, cpf, type, paymethod, adress, syndicate)
        print('Novo empregado adicionado:')
        Sys.CurrentEmployee.ShowInfo()


    def RemoveEmployee():
        if Sys.EmployeeNum > 0:
            id = input('Digite o cpf do funcionário que deseja remover: ')
            if Sys.SetCurrent(id):
                Sys.RemoveEmployee()
            else: print('FUNCIONÁRIO INVÁLIDO')


    def EditEmployee():
        print('--------------')
        if Sys.ShowEmployees():
            id = int(input('Seleione o empregado a ser editado: '))
            current = Sys.SetCurrent(id)
            if current != False:
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
                    print('1.Editar nome\n2.Alterar tipo\n3.Alterar método de pagamento\n4.Editar endereço\n5.Alterar sindicato\n6. SAIR')
                    option = int(input())
                    if option == 1:
                        current.SetInfo(name = input('Digite o novo nome: '))
                    if option == 2:
                        current.SetInfo(type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: ')))
                    if option == 3:
                        current.SetInfo(paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: ')))
                    if option == 4: editAdress()
                    if option == 5:
                        if current.syndicate:
                            if input('Funcionário pertence ao sindicato, remover?[s/n]: ') in 'Ss': current.syndicate = False
                        else: 
                            if input('Funcionário não pertence ao sindicato, adicionar?[s/n]: ') in 'Ss': current.syndicate = True
                    if option == 6: break

                print('--EMPREGADO EDITADO--')
                current.ShowInfo()
            else: print('FUNCIONÁRIO INVÁLIDO')

    def RegInfo():      
        if Sys.ShowEmployees():
                id = int(input('Selecione o funcionário para registrar informação: '))
                current = Sys.SetCurrent(id)
                if current != False:

                    while True:
                        print('--SELECIONE UMA OPÇÃO--')
                        print('1.Registrar venda\n2.Registrar ponto\n3.Registrar taxa de sindicato\n4.Voltar')
                        option = int(input())
                        
                        if option == 1:
                            value = float(input('Insira o valor: '))
                            current.NewSale(value, time.asctime())
                        if option == 2:
                            current.RegPonto(time.asctime())
                        if option == 3:
                            value = float(input('Insira o valor da taxa: '))
                            current.NovaTaxa(value)
                        if option == 4: break
                else: print('FUNCIONÁRIO INVÁLIDO')


while True:
    print('--SELLECIONE UMA OPÇÃO--')
    print('1.Adicionar empregado\n2.Remover empregado\n3.Editar empregado\n4.Listar empregados\n5.Registrar informações\n6.SAIR')
    option = int(input())
    if option == 1: menu.AddEmployee()
    if option == 2: menu.RemoveEmployee()
    if option == 3: menu.EditEmployee()
    if option == 4: Sys.ShowEmployees()
    if option == 5: menu.RegInfo()
    if option == 6: break

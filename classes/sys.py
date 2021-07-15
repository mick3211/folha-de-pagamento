from classes.employee import Person, Hourly, Salaried, Commissioned


class Sys():
    EmployeeList = {}
    EmployeeNum = 0
    CurrentEmployee = None

    def ShowEmployees():
        if Sys.EmployeeNum > 0:
            for i, employee in Sys.EmployeeList.items():
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

    def AddEmployee(name, cpf, type, paymethod, adress, syndicate):
        if type == 1: new_employee = Hourly()
        if type == 2: new_employee = Salaried()
        if type == 3: new_employee = Commissioned()
        new_employee.SetInfo(name, cpf, paymethod, syndicate)
        new_employee.SetAdress(*adress)
        Sys.EmployeeList[cpf] = new_employee
        Sys.EmployeeNum += 1
        Sys.SetCurrent(cpf)

    def RemoveEmployee(id = None):
        if id == None: return Sys.EmployeeList.popitem()
        else: return Sys.EmployeeList.pop(id)
    
    def printInfo(id):
        current = Sys.SetCurrent(id)
        if current != False:
            info = current.getInfo(all = True)
            if info['type'] == 1: type = "Horista"
            if info['type'] == 2: type = "Assalariado"
            if info['type'] == 3: type = "Comissionado"
            if info['paymethod'] == 1: paymethod = "Cheque pelos Correios"
            if info['paymethod'] == 2: paymethod = "Cheque em mãos"
            if info['paymethod'] == 3: paymethod = "Depósito bancário"
            print('Nome:', info['name'])
            print('CPF:', info['cpf'])
            print('Tipo:', type)
            print('Método de pagamento:', paymethod)
            if info['syndicate']: print('Pertence ao sindicato')
            else: print('Não pertence ao sindicato')
        else: return False

    def printAdress(id):
        current = Sys.SetCurrent(id)
        if current != False:
            adress = current.getAdress(all = True)
            print('CEP:', adress['cep'])
            print('Rua:', adress['rua'])
            print('Número:', adress['numero'])
            print('Bairro', adress['bairro'])
            print('Cidade:', adress['cidade'])
            print('Estado:', adress['estado'])
        else: return False
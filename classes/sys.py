from classes.employee import Person, Hourly, Salaried, Commissioned
import time
from copy import deepcopy


class Sys():
    EmployeeList = {}
    EmployeeNum = 0
    last_employee = Person()
    last_action = 0
    agendas = [(2, 1, 6), (2, 2, 6), (1, 30)]

    def undo():
        if Sys.last_action == 1:
            Sys.RemoveEmployee()
            return 1
        elif Sys.last_action == 2:
            Sys.appendEmployee(Sys.last_employee)
            return 2
        elif Sys.last_action == 3:
            Sys.restoreEmployee()
            return 3

    def ShowEmployees():
        if Sys.EmployeeNum > 0:
            for i, employee in Sys.EmployeeList.items():
                print(f'{i}:', employee.name)
            return True
        else:
            print('SEM FUNCIONÁRIOS CADASTRADOS')
            return False

    def isEmployee(id):
        if id in Sys.EmployeeList.keys(): return Sys.EmployeeList[id]
        else: return False

    def setLastEmployee(id):
        if Sys.isEmployee(id) != False:
            Sys.last_employee = deepcopy(Sys.EmployeeList[id])
        
    def AddEmployee(name, cpf, type, paymethod, adress, syndicate, taxa):
        if type == 1: new_employee = Hourly()
        elif type == 2: new_employee = Salaried()
        elif type == 3: new_employee = Commissioned()
        new_employee.SetInfo(name, cpf, paymethod, syndicate, taxa)
        new_employee.SetAdress(*adress)
        Sys.EmployeeList[cpf] = new_employee
        Sys.setLastEmployee(cpf)

        Sys.EmployeeNum += 1
        Sys.last_action = 1

    def appendEmployee(employee):
        Sys.EmployeeList.update({employee.cpf: employee})
        Sys.EmployeeNum += 1
        Sys.last_action = 1

    def RemoveEmployee(id = None):
        Sys.last_action = 2
        if Sys.EmployeeNum > 0:
            Sys.EmployeeNum = Sys.EmployeeNum - 1
            if id == None: Sys.last_employee = Sys.EmployeeList.popitem()[1]
            else: Sys.last_employee = Sys.EmployeeList.pop(id)
        else: return False

    def restoreEmployee():
        temp = Sys.EmployeeList.get(Sys.last_employee.cpf)
        Sys.EmployeeList.update({Sys.last_employee.cpf: Sys.last_employee})
        Sys.last_employee = temp

    def setAdress(id, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if Sys.isEmployee(id) != False:
            Sys.EmployeeList[id].SetAdress(cep, numero, rua, bairro, cidade, estado)
            return True
        else: return False

    def setInfo(id, name = None, cpf = None, paymethod = None, syndicate = None, taxa = None):
        if Sys.isEmployee(id) != False:
            Sys.EmployeeList[id].SetInfo(name, cpf, paymethod, syndicate, taxa)
            return True
        else: return False

    def setType(id, type):
        if Sys.EmployeeList[id].type != type:
            if type == 1: copy = Hourly()
            if type == 2: copy = Salaried()
            if type == 3: copy = Commissioned()
            info_list = Sys.EmployeeList[id].getInfo(type = False).values()
            adress_list = Sys.EmployeeList[id].getAdress().values()
            copy.SetInfo(*info_list)
            copy.SetAdress(*adress_list)
            Sys.EmployeeList.pop(id)
            Sys.EmployeeList[id] = copy
        else: return False

    def regTaxa(id , taxa):
        current = Sys.isEmployee(id)
        if current != False:
            if current.syndicate != False:
                current.syndicate.serv_tax.append(taxa)
                Sys.last_action = 3
                return True
        return False

    def regPonto(id, date):
        if Sys.isEmployee(id) != False:
            if Sys.EmployeeList[id].type == 1:
                Sys.setLastEmployee(id)
                Sys.last_action = 3
                return Sys.EmployeeList[id].regPonto(date)
            else: return False
        else: return False
    
    def regSale(id , value, date):
        if Sys.isEmployee(id) != False:
            if Sys.EmployeeList[id].type == 3:
                Sys.setLastEmployee(id)
                Sys.EmployeeList[id].regSale(value, date)
                Sys.last_action = 3
                return True
            else: return False
        else: return False

    def addAgenda(tipo, dia, frequencia = None):
        if tipo == 2: Sys.agendas.append((tipo, frequencia, dia))
        elif tipo == 1: Sys.agendas.append((tipo, dia))
        print(Sys.agendas)
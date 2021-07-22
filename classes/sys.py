from classes.employee import Person, Hourly, Salaried, Commissioned
import time
from copy import deepcopy


class Sys():
    EmployeeList = {}
    EmployeeNum = 0
    CurrentEmployee = None
    last_employee = None
    last_action = None

    def undo():
        if Sys.last_action == 1:
            Sys.last_employee = Sys.RemoveEmployee()[1]
            return 1
        if Sys.last_action == 2:
            Sys.appendEmployee(Sys.last_employee)
            return 2
        if Sys.last_action == 3:
            Sys.restoreEmployee()
            return 3
        if Sys.last_action == 4:
            Sys.CurrentEmployee.hisPontos.pop()
            print(Sys.CurrentEmployee.hisPontos)
            return 4
        if Sys.last_action == 5:
            Sys.CurrentEmployee.hisVendas.pop()
            print(Sys.CurrentEmployee.hisVendas)
            return 5

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

    def setLastEmployeep():
        Sys.last_employee = deepcopy(Sys.CurrentEmployee)
        
    def AddEmployee(name, cpf, type, paymethod, adress, syndicate):
        if type == 1: new_employee = Hourly()
        if type == 2: new_employee = Salaried()
        if type == 3: new_employee = Commissioned()
        new_employee.SetInfo(name, cpf, paymethod, syndicate)
        new_employee.SetAdress(*adress)
        Sys.EmployeeList[cpf] = new_employee
        Sys.SetCurrent(cpf)

        Sys.EmployeeNum += 1
        Sys.last_action = 1

    def appendEmployee(employee):
        Sys.EmployeeList.update({employee.cpf: employee})
        Sys.employeeNum += 1
        Sys.last_action = 1

    def RemoveEmployee(id = None):
        Sys.last_action = 2
        if Sys.EmployeeNum > 0:
            Sys.EmployeeNum = Sys.EmployeeNum - 1
            if id == None: Sys.last_employee = Sys.EmployeeList.popitem()
            else: Sys.last_employee = Sys.EmployeeList.pop(id)
        else: return False

    def restoreEmployee():
        temp = Sys.CurrentEmployee
        Sys.EmployeeList.update({Sys.last_employee.cpf: Sys.last_employee})
        Sys.last_employee = temp
        Sys.CurrentEmployee = Sys.last_employee

    def setAdress(id, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if Sys.SetCurrent(id):
            Sys.CurrentEmployee.SetAdress(cep, numero, rua, bairro, cidade, estado)
            return True
        else: return False

    def setInfo(id, name = None, cpf = None, paymethod = None, syndicate = None, taxa = 30):
        if Sys.SetCurrent(id):
            Sys.CurrentEmployee.SetInfo(name, cpf, paymethod, syndicate, taxa)
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

    def regPonto(id, date):
        if Sys.SetCurrent(id) != False:
            if Sys.CurrentEmployee.type == 1:
                Sys.CurrentEmployee.regPonto(date)
                Sys.last_action = 6
                return True
            else: return False
        else: return False
    
    def regSale(id , value):
        if Sys.SetCurrent(id) != False:
            if Sys.CurrentEmployee.type == 3:
                Sys.CurrentEmployee.regSale(value)
                Sys.last_action = 7
                return True
            else: return False
        else: return False
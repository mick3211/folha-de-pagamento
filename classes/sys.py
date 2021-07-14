from classes.person import Person, Hourly, Salaried, Commissioned

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
        if id == None: return Sys.EmployeeList.popitem()
        else: return Sys.EmployeeList.pop(id)
from classes.menu import Menu
from classes.sys import Sys


while True:
    print('--SELLECIONE UMA OPÇÃO--')
    print('1.Adicionar empregado\n2.Remover empregado\n3.Editar empregado\n4.Listar empregados\n5.Registrar informações\n6.SAIR')
    option = int(input())
    if option == 1: Menu.AddEmployee()
    if option == 2: Menu.RemoveEmployee()
    if option == 3: Menu.EditEmployee()
    if option == 4: Sys.ShowEmployees()
    if option == 5: Menu.RegInfo()
    if option == 6: break

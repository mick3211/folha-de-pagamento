from classes.menu import Menu
from classes.sys import Sys


while True:
    print('--SELLECIONE UMA OPÇÃO--')
    print('1.Adicionar empregado\n2.Editar empregado\n3.Listar empregados\n4.Registrar informações\n5.Undo/Redo\n6.SAIR')
    option = int(input())
    if option == 1: Menu.AddEmployee()
    if option == 2: Menu.EditEmployee()
    if option == 3: Sys.ShowEmployees()
    if option == 4: Menu.RegInfo()
    #bug undo ao mudar o tipo
    if option == 5: Sys.undo()
    if option == 6: break

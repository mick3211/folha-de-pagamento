from classes.menu import Menu
from classes.sys import Sys


while True:
    print('--SELLECIONE UMA OPÇÃO--')
    print('1.Adicionar empregado\n2.Editar empregado\n3.Listar empregados\n4.Registrar informações\n5.Undo/Redo\n6.Adicionar agenda de pagamento\n7.Rodar folha de pagamento\n8.SAIR')
    option = input()
    if option == '1': Menu.AddEmployee()
    if option == '2': Menu.EditEmployee()
    if option == '3': Sys.ShowEmployees()
    if option == '4': Menu.RegInfo()
    if option == '5': Menu.undo()
    if option == '6': Menu.addAgenda()
    if option == '7': Menu.print_payment_schedule()
    if option == '8': break

from webbrowser import WindowsDefault
from PySimpleGUI.PySimpleGUI import Window
from classes.menu import Menu
from classes.sys import Sys
from classes.layouts import HOME_LAYOUT
import PySimpleGUI as sg


WINDOW = sg.Window('Folha de pagamento', HOME_LAYOUT, use_default_focus=False)


while True:
    event, values = WINDOW.read()

    if event == sg.WIN_CLOSED or event == "Sair": break
    if event == 'Adicionar empregado': Menu.add_employee()
    if event == 'Editar empregado':
        select = Menu.select_employee()
        if select != False: Menu.edit_employee(select)
    if event == 'Registrar informações': Sys.ShowEmployees()

WINDOW.close(); del WINDOW
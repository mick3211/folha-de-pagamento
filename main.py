from webbrowser import WindowsDefault
from PySimpleGUI.PySimpleGUI import Window
import PySimpleGUI as sg
from classes.menu import Menu
from classes.layouts import home_layout


window = sg.Window('Folha de pagamento', home_layout(), use_default_focus=False)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Sair": break
    if event == 'Adicionar empregado': Menu.add_employee()
    if event == 'Undo/redo': Menu.undo()
    if event == 'agenda': Menu.add_agenda()
    if event == 'pay': Menu.pay_schedule()
    if event == 'Editar empregado':
        select = Menu.select_employee()
        if select != False: Menu.edit_employee(select)
    if event == 'Registrar informações':
        select = Menu.select_employee()
        if select != False: Menu.reg_info(select)

window.close(); del window
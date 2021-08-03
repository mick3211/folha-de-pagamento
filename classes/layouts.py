from typing import DefaultDict
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, Text


PAYMETHODS = {1: 'Cheque pelos Correios', 2: 'Cheque em mãos', 3: 'Depósito bancário'}
TYPES = {1: 'Horista', 2: 'Assalariado', 3: 'Comissionado'}


HOME_LAYOUT = [
    [sg.Button('Adicionar empregado', size=(30,2))],
    [sg.Button('Editar empregado', size=(30,2))],
    [sg.Button('Registrar informações', size=(30,2))],
    [sg.Button('Sair', button_color = 'red', size=(30,2))]
]

def add_employee_layout():
    return [
        [sg.Frame('Informações pessoais', [
            [sg.Text('Nome:')],
            [sg.Input(key = 'name')],
            [sg.Text('CPF:')],
            [sg.Input(key = 'cpf')],
        ], key='personal_info')],
        [sg.Frame('Definições do empregado', [
            [sg.Text('Tipo:')],
            [sg.Combo(['Horista', 'Assalariado', 'Comissionado'], key='type', default_value='Horista')],
            [sg.Text('Método de pagamento:')], 
            [sg.Combo(['Cheque pelos Correios', 'Cheque em mãos', 'Depósito bancário'], key='paymethod', default_value='Cheque em mãos')],
            [sg.Text('Faz parte do sindicato?')],
            [sg.Radio('Sim', group_id='syn', key='syndicate', enable_events=True), sg.Radio('Não', group_id='syn', key='not_syndicate', default=True, enable_events=True)],
            [sg.Text('Valor da taxa sindical:', key='syn_text', visible=False)],
            [sg.Input(key='taxa', visible=False)],
        ], key='employee_info')],
        [sg.Frame('Endereço', [
                [sg.Text('Rua:', pad=((5,265), (0,0))), sg.Text('N°:')],
                [sg.Input(key='rua', size=(41,1)), sg.Input(key='numero', size=(3,1))],
                [sg.Text('CEP:', pad=((5,125), (0,0))), sg.Text('Bairro:')],
                [sg.Input(key='cep', size=(22,1)), sg.Input(key='bairro', size=(22,1))],
                [sg.Text('Cidade:', pad=((5,115),(0,0))), sg.Text('Estado:')],
                [sg.Input(key='cidade', size=(22,1)), sg.Input(key='estado', size=(22,1))]
            ], key='adress')
        ],
        [sg.Button('Voltar'), sg.Button('Adicionar')]
    ]

def edit_employee_layout(employee):

    info_list = employee.getInfo()
    adress_list = employee.getAdress()

    return [
        [sg.Frame('Informações pessoais', [
            [sg.Text('Nome:')],
            [sg.Input(info_list['name'], key = 'name')],
        ], key='personal_info')],
        [sg.Frame('Definições do empregado', [
            [sg.Text('Tipo:')],
            [sg.Combo(['Horista', 'Assalariado', 'Comissionado'], key='type', default_value=TYPES[info_list['type']])],
            [sg.Text('Método de pagamento:')], 
            [sg.Combo(['Cheque pelos Correios', 'Cheque em mãos', 'Depósito bancário'], key='paymethod', default_value=PAYMETHODS[info_list['paymethod']])],
            [sg.Text('Faz parte do sindicato?')],
            [sg.Radio('Sim', group_id='syn', key='syndicate', enable_events=True, default=False if not info_list['syndicate'] else True),
                sg.Radio('Não', group_id='syn', key='not_syndicate', enable_events=True, default=True if not info_list['syndicate'] else False)],
            [sg.Text('Valor da taxa sindical:', key='syn_text', visible=False if not info_list['syndicate'] else True)],
            [sg.Input(employee.syndicate.syn_tax if info_list['syndicate'] != False else '', key='taxa', visible=False if not info_list['syndicate'] else True)],
        ], key='employee_info')],
        [sg.Frame('Endereço', [
                [sg.Text('Rua:', pad=((5,265), (0,0))), sg.Text('N°:')],
                [sg.Input(adress_list['rua'], key='rua', size=(41,1)), sg.Input(adress_list['numero'], key='numero', size=(3,1))],
                [sg.Text('CEP:', pad=((5,125), (0,0))), sg.Text('Bairro:')],
                [sg.Input(adress_list['cep'], key='cep', size=(22,1)), sg.Input(adress_list['bairro'], key='bairro', size=(22,1))],
                [sg.Text('Cidade:', pad=((5,115),(0,0))), sg.Text('Estado:')],
                [sg.Input(adress_list['cidade'], key='cidade', size=(22,1)), sg.Input(adress_list['estado'], key='estado', size=(22,1))]
            ], key='adress')
        ],
        [sg.Button('EXCLUIR EMPREGADO', button_color = 'red')],
        [sg.Button('Voltar'), sg.Button('Salvar')]
    ]

def select_employee_layout(employee_list):

    i = list(employee_list.keys())

    return [
        [sg.Text('Selecione o empregado:')],
        [sg.Combo(i, key='selected_employee', default_value=i[0])],
        [sg.Button('Selecionar')],
    ]

#def reg_info_layout(employee):


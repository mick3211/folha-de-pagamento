from typing import DefaultDict
import PySimpleGUI as sg
import time
from PySimpleGUI.PySimpleGUI import Input, Text
from classes.sys import Sys


PAYMETHODS = {1: 'Cheque pelos Correios', 2: 'Cheque em mãos', 3: 'Depósito bancário'}
TYPES = {1: 'Horista', 2: 'Assalariado', 3: 'Comissionado'}
DIAS = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')


def home_layout():
    return (
        [sg.Menu([['Opções','Undo/redo']])],
        [sg.Button('Adicionar empregado', size=(30,2))],
        [sg.Button('Editar empregado', size=(30,2))],
        [sg.Button('Registrar informações', size=(30,2))],
        [sg.Button('Adicionar agenda de pagamento', size=(30,2), key='agenda')],
        [sg.Button('Rodar folha de pagamento', size=(30,2), key='pay')],
        [sg.Button('Sair', button_color = 'red', size=(30,2))]
    )

def add_employee_layout():
    return (
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
            [sg.Input(0, key='taxa', visible=False, size=(10,1))],
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
    )

def edit_employee_layout(employee):

    info_list = employee.getInfo()
    adress_list = employee.getAdress()
    agendas = ['Não alterar']

    for n, i in enumerate(Sys.agendas):
        if i[0] == 1: agendas.append(f'{n}. Mesalmente, todo dia {i[1]}')
        else: agendas.append(f'{n}. A cada {i[1]} semanas toda {DIAS[i[2]]}')

    return (
        [sg.Frame('Informações pessoais', [
            [sg.Text('Nome:')],
            [sg.Input(info_list['name'], key = 'name')],
        ], key='personal_info')],
        [sg.Frame('Definições do empregado', [
            [sg.Text('Tipo:')],
            [sg.Combo(['Horista', 'Assalariado', 'Comissionado'], key='type', default_value=TYPES[info_list['type']])],
            [sg.Text('Método de pagamento:')], 
            [sg.Combo(['Cheque pelos Correios', 'Cheque em mãos', 'Depósito bancário'], key='paymethod', default_value=PAYMETHODS[info_list['paymethod']])],
            [sg.Text('Agenda de pagamento (aplicado após o próximo pagamento)')],
            [sg.Combo(agendas, agendas[0], key='agenda')],
            [sg.Text('Faz parte do sindicato?')],
            [sg.Radio('Sim', group_id='syn', key='syndicate', enable_events=True, default=False if not info_list['syndicate'] else True),
                sg.Radio('Não', group_id='syn', key='not_syndicate', enable_events=True, default=True if not info_list['syndicate'] else False)],
            [sg.Text('Valor da taxa sindical:', key='syn_text', visible=False if not info_list['syndicate'] else True)],
            [sg.Input(employee.syndicate.syn_tax if info_list['syndicate'] != False else 0, key='taxa', visible=False if not info_list['syndicate'] else True, size=(10,1))],
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
    )

def select_employee_layout(employee_list):

    i = list(employee_list.keys())

    return (
        [sg.Text('Selecione o empregado:')],
        [sg.Combo(i, key='selected_employee', default_value=i[0])],
        [sg.Button('Selecionar')],
    )

def reg_info_layout(employee):

    serv = [[sg.Frame('Lançar taxa de serviço', [
                [sg.Input(key='serv_taxe'), sg.Button('Lançar')],
            ], visible=False if not employee.syndicate else True)]]

    if employee.type == 1:
        return (
            [sg.Button('Registrar entrada' if employee.ini == None else 'Registrar saída', key='ponto')],
            serv,
            [sg.Button('Voltar')]
        )

    elif employee.type == 3:
        return (
            [sg.Frame('Lançar venda',[
                [sg.Input(key='sale_value'), sg.Button('Lançar', key='venda')]
            ])],
            serv,
            [sg.Button('Voltar')]
        )

    else:
        if not employee.syndicate:
            return (
                [sg.Text('Não há informações a serem registradas para o funcionário selecionado')],
                [sg.Button('Voltar')]
            )
        else: return serv

def add_agenda_layout():
    return (
        [sg.Radio('Semanal', 'ag1', default=True, key='type1', enable_events=True)],
        [sg.Frame('A cada', [
            [sg.Combo([1, 2, 3], 1, key = 'ag2'), sg.Text('Semana(as)')],
            [sg.Text('Toda:'), sg.Combo(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'], 'Segunda', key='ag3'), sg.Button('Adicionar', key='add2')]
        ], key='weeks')],
        [sg.Radio('Mensal', 'ag1', key='type2', enable_events=True)],
        [sg.Frame('Todo dia', [
            [sg.Combo([i for i in range(1, 31)], 1, key='day'), sg.Button('Adicionar', key='add1')]
        ], key='days', visible=False)],
        [sg.Button('Voltar')]
    )

def pay_schedule_layout():
    current_date = time.localtime()

    return (
        [sg.Text(f'Hoje {time.strftime("%a, %d/%m/%Y", current_date)}', font=('arial', 15), justification='center')],
        [sg.Output(size=(100,20))],
        [sg.Button('Rodar', button_color='green', size=(10,2)), sg.Button('Próximo dia', key='next')],
        [sg.Button('Voltar'), sg.Button('Pagar todos')]
    )
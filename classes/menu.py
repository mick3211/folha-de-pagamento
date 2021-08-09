from PySimpleGUI.PySimpleGUI import popup
from classes.sys import Sys
from classes.employee import Person
from classes.layouts import add_employee_layout, select_employee_layout, edit_employee_layout, reg_info_layout, add_agenda_layout, pay_schedule_layout
import PySimpleGUI as sg
import time


ERROR1 = 'FUNCIONÁRIO INVÁLIDO'
ERROR2 = 'SEM FUNCIONÁRIOS CADASTRADOS'
DIAS = {'Segunda': 0, 'Terça': 1, 'Quarta': 2, 'Quinta': 3, 'Sexta': 4}
PAYMETHODS = {'Cheque pelos Correios': 1, 'Cheque em mãos':2, 'Depósito bancário':3}
TYPES = {'Horista': 1, 'Assalariado': 2, 'Comissionado': 3}


class Menu():

    def printData(id, info = True, adress = True):
        if Sys.EmployeeNum > 0:
            current = Sys.isEmployee(id)
            if current != False:

                if info:
                    info_list = current.getInfo()
                    print('DADOS:')
                    print('Nome:', info_list['name'])
                    print('CPF:', info_list['cpf'])
                    print('Tipo:', list(TYPES.keys())[info_list['type'] - 1])
                    print('Método de pagamento:', list(PAYMETHODS.keys())[info_list['paymethod'] - 1])
                    if info_list['syndicate'] != False:
                        print('Pertence ao sindicato')
                        print(f'Taxa sindical: R${current.syndicate.syn_tax}')
                    else: print('Não pertence ao sindicato')
                    print(current.agenda)
                    print(current.new_agenda)
                    print('Salario:', info_list['salary'])
                    print('Proximo pagamento:', current.next_payday)

                if adress:
                    print('ENDEREÇO:')
                    adress_list = current.getAdress()
                    print('CEP:', adress_list['cep'])
                    print('Rua:', adress_list['rua'])
                    print('Número:', adress_list['numero'])
                    print('Bairro', adress_list['bairro'])
                    print('Cidade:', adress_list['cidade'])
                    print('Estado:', adress_list['estado'])

            else: print(ERROR1)
        else: print(ERROR2)

    def add_employee():

        window = sg.Window('Novo empregado', add_employee_layout())

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Voltar": break

            if event == 'syndicate':
                window['syn_text'].update(visible=True)
                window['taxa'].update(visible=True)

            if event == 'not_syndicate':
                window['syn_text'].update(visible=False)
                window['taxa'].update(visible=False)

            if values['type'] == 'Horista':
                window['t2'].update('Valor do salário hora:')
            else: window['t2'].update('Valor do salário mês:')

            if values['type'] == 'Comissionado':
                window['com'].update(visible=True)
            else:
                window['com'].update(visible=False)

            if event == 'Adicionar':
                name = values['name']
                cpf = values['cpf']
                syndicate = True if values['syndicate'] == True else False
                adress = (values['cep'], values['numero'], values['rua'], values['bairro'], values['cidade'], values['estado'])

                try: type = TYPES[values['type']]
                except: sg.popup('TIPO INVÁLIDO', title='ERRO')
                else:
                    try: paymethod = PAYMETHODS[values['paymethod']]
                    except: sg.popup('MÉTODO DE PAGAMENTO INVÁLIDO', title='ERRO')
                    else:
                        try: taxa = float(values['taxa']) if syndicate else None
                        except: sg.popup('VALOR DA TAXA SINDICAL INVÁLIDO', title='ERRO')
                        else:
                            try: salary = float(values['salary'])
                            except: sg.popup('VALOR DO SALÁRIO INVÁLIDO')
                            else:
                                try: comissao = float(values['comissao'])/100 if values['type'] == 'Comissionado' else None
                                except: sg.popup('VALOR DA COMISSÃO INVÁLIDO')
                                else:
                                    if cpf == '' or cpf in Sys.EmployeeList.keys(): sg.popup('CPF JÁ CADASTRADO!', title='ERRO')
                                    elif name == '': sg,popup('INSIRA UM NOME VÁLIDO', title='ERRO')
                                    else:
                                        Sys.AddEmployee(name, cpf, type, paymethod, adress, syndicate, taxa, salary, comissao)
                                        sg.popup('Empregado adicionado')
                                        Menu.printData(cpf)
                                        break

        window.close(); del window

    def select_employee():

        if Sys.EmployeeNum == 0:
            sg.popup('SEM FUNCIONÁRIOS CADASTRADOS!', title='ERRO')
            return False

        else:
            window = sg.Window('Selecionar empregado', select_employee_layout(Sys.EmployeeList))

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED or event == "Voltar":
                    window.close(); del window
                    return False
                if event == 'Selecionar':
                    window.close(); del window
                    if values['selected_employee'] in Sys.EmployeeList.keys():
                        return values['selected_employee']
                    else: sg.popup('FUNCIONÁRIO INVÁLIDO!', title='ERRO')

    def edit_employee(id):
        window = sg.Window('Editar empregado', edit_employee_layout(Sys.getEmployee(id)), enable_close_attempted_event=True)

        while True:
            event, values = window.read()
            
            if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Voltar') and sg.popup_yes_no('Sair sem salvar?') == 'Yes':
                break
            if event == 'EXCLUIR EMPREGADO' and sg.popup_yes_no('Tem certeza que quer deletar o funcionário?') == 'Yes':
                if Sys.RemoveEmployee(id):
                    sg.popup('Funcionário removido')
                    break
                else: sg.popup('Não foi possível remover o funionário')

            if event == 'syndicate':
                window['syn_text'].update(visible=True)
                window['taxa'].update(visible=True)

            if event == 'not_syndicate':
                window['syn_text'].update(visible=False)
                window['taxa'].update(visible=False)

            if event == 'Salvar':
                name = values['name']
                type = TYPES[values['type']]
                paymethod = PAYMETHODS[values['paymethod']]
                syndicate = False if not values['syndicate'] else True
                adress = (values['cep'], values['numero'], values['rua'], values['bairro'], values['cidade'], values['estado'])

                if values['agenda'] == 'Não alterar': agenda = None
                else:
                    agenda = values['agenda'].split('.')
                    agenda = int(agenda[0])

                try:
                    taxa = float(values['taxa']) if syndicate else None
                except:
                    sg.popup('VALOR DA TAXA SINDICAL INVÁLIDO', title='ERRO')
                else:
                    if Sys.setInfo(id, name, None, paymethod, syndicate, taxa, type, adress, agenda):
                        sg.popup('Alterações Salvas', title = 'Confirmação')
                        Menu.printData(id)
                    else: sg.popup('Não foi possível salvar as alterações', title='ERRO')
                    break

        window.close(); del window

    def reg_info(id):

        employee = Sys.getEmployee(id)
        window = sg.Window('Registrar informações', layout=reg_info_layout(employee), use_default_focus=False)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Voltar': break

            if event == 'ponto':
                if Sys.regPonto(id, time.time()):
                    sg.popup('Ponto registrado')
                else: sg.popup('Não foi possível registrar o ponto', title='ERRO')
                break

            if event == 'venda':
                try:
                    sale= float(values['sale_value'])
                except:
                    sg.popup('VALOR DA VENDA INVÁLIDO', title='ERRO')
                else:
                    if Sys.regSale(id, sale, time.asctime()):
                        sg.popup(f'Venda no valor de R${sale} registrada', title='Venda registrada')
                    else: sg.popup('Não foi possível registrar a venda', title='ERRO')

            if event == 'Lançar':
                try:
                    serv_taxe = float(values['serv_taxe'])
                except:
                    sg.popup('VALOR DA TAXA INVÁLIDO', title='ERRO')
                else:
                    if Sys.regTaxa(id, serv_taxe):
                        sg.popup(f'Taxa de serviço no valor de R${serv_taxe} registrada', title='Taxa registrada')
                    else: sg.popup('Não foi possível registrar a taxa de serviço', title='ERRO')

        window.close(); del window

    def undo():
        if Sys.last_action != 0:
            act = Sys.undo()
            if act == 1: sg.popup('Funcionário removido', title='Desfazer')
            elif act == 2: sg.popup('Funcionário readicionado', title='Refazer')
            elif act == 3: sg.popup('Ação restaurada', title='Refazer')
            elif act == 4: sg.popup('Ação desfeita', title='Desfazer')
        else: sg.popup('Sem ações')

    def add_agenda():
        window = sg.Window('Adicionar agenda', layout=add_agenda_layout())

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Voltar': break

            if event == 'type2':
                window['weeks'].update(visible=False)
                window['days'].update(visible=True)

            if event == 'type1':
                window['weeks'].update(visible=True)
                window['days'].update(visible=False)

            if event == 'add1':
                Sys.addAgenda(1, values['day'])
                print(Sys.agendas)
                sg.popup('Agenda adicionada')

            if event == 'add2':
                Sys.addAgenda(2, DIAS[values['ag3']], values['ag2'])
                print(Sys.agendas)
                sg.popup('Agenda adicionada')

        window.close(); del window

    def pay_schedule():
        window = sg.Window('Folha de pagamento', layout=pay_schedule_layout(), use_default_focus=False)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Voltar': break
            if event == 'Rodar': pending = Menu.print_payment_schedule()
            if event == 'next' and Sys.EmployeeNum > 0: pending = Menu.print_payment_schedule(next=True)
            if event == 'pay':
                for e in pending:
                    print('pagando...')
                    e.pay()
        
        window.close(); del window
        
    def print_payment_schedule(day = time.time(), next = False):
            
        current_date = time.localtime(day)
        pending_employees = list()
        print(f'Hoje {time.strftime("%a, %d/%m/%Y", current_date)}')
        print('--SALÁRIOS DEVIDOS--')

        for e in Sys.EmployeeList.values():

            if e.next_payday.tm_yday == current_date.tm_yday:
                pending_employees.append(e)
                

        for i, e in enumerate(pending_employees):
            print(f'{i}.{e.name}: R${e.accumulated_payment()}/{list(PAYMETHODS.keys())[e.paymethod - 1]}')

        if len(pending_employees) == 0: 
            print('Sem pagamentos pendentes para hoje')
            if next:
                return Menu.print_payment_schedule(time.mktime(current_date) + 86400, True)
        return pending_employees

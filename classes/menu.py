from classes.sys import Sys
from classes.employee import Person
from classes.layouts import add_employee_layout, select_employee_layout, edit_employee_layout
import PySimpleGUI as sg
import time


ERROR1 = 'FUNCIONÁRIO INVÁLIDO'
ERROR2 = 'SEM FUNCIONÁRIOS CADASTRADOS'
DIAS = {'segunda': 0, 'terça': 1, 'quarta': 2, 'quinta': 3, 'sexta': 4, 'sábado': 5, 'domingo': 6}
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

            if event == 'Adicionar':
                name = values['name']
                cpf = values['cpf']
                type = TYPES[values['type']]
                paymethod = PAYMETHODS[values['paymethod']]
                syndicate = True if values['syndicate'] == True else False
                taxa = values['taxa'] if syndicate else None
                adress = (values['cep'], values['numero'], values['rua'], values['bairro'], values['cidade'], values['estado'])
                
                if cpf == '' or cpf in Sys.EmployeeList.keys(): sg.popup('CPF JÁ CADASTRADO!')
                else:
                    Sys.AddEmployee(name, cpf, type, paymethod, adress, syndicate, taxa)
                    sg.popup('Empregado adicionado')
                    Menu.printData(cpf)
                    break

        window.close(); del window

    def select_employee():

        if Sys.EmployeeNum == 0:
            sg.popup('SEM FUNCIONÁRIOS CADASTRADOS!', title='Erro')
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
                taxa = values['taxa'] if syndicate else None
                adress = (values['cep'], values['numero'], values['rua'], values['bairro'], values['cidade'], values['estado'])

                if type != Sys.getEmployee(id).type: Sys.setType(id, type)

                Sys.setInfo(id, name, None, paymethod, syndicate, taxa)
                Sys.setAdress(id, *adress)
                sg.popup('Alterações Salvas')
                Menu.printData(id)
                break

        window.close(); del window

    def RegInfo():      
        if Sys.EmployeeNum > 0:
            id = input('Insira o cpf do funcionário: ')
            current = Sys.isEmployee(id)
            if current != False:
                while True:

                    print('1.Lançar taxa de serviço')
                    if current.type == 1: print('2.Registrar ponto')
                    if current.type == 3: print('2.Lançar venda')
                    print('3.VOLTAR')

                    op = input('Escolha uma opção: ')

                    if op == '1':
                        if False not in current.getInfo(syndicate = True).values():
                            if Sys.regTaxa(current.cpf, float(input('Insira o valor da taxa: '))):
                                print('Taxa resgistrada')
                            else: print('Taxa não registrada')
                        else: print('FUNCIONÁRIO NÃO PERTENCE AO SINDICATO')

                    if op == '2':
                        if current.type == 1:
                            p = Sys.regPonto(id, time.time())
                            if p == 1: print('Entrada registrada')
                            elif p == 2: print('Saída registrada')
                            elif p == False: print('PONTO NÃO REGISTRADO')

                        if current.type == 3:
                            if Sys.regSale(id, int(input('Insira o valor da venda: ')), time.asctime()):
                                print('Venda resgistrada')
                            else: print('Venda não registrada')

                    if op == '3': break

            else: print(ERROR1)
        else: print(ERROR2)

    def undo():
        if Sys.last_action != 0:
            act = Sys.undo()
            if act == 1: print('Funcionário removido')
            if act == 2: print('Funcionário readicionado')
            if act == 3: print('Informações restauradas')
        else: print('Sem ações')

    def addAgenda():
        print('CRIAÇÃO DE NOVA AGENDA')
        agenda = input('Digite o tipo de agenda que deseja criar: ').split()

        if agenda[0] in ('semanalmente', 'semanal', 'Semanalmente', 'Semanal'):
            if agenda[1] in ('1', '2', '3'):
                if agenda[2] in DIAS.keys():
                    Sys.addAgenda(2, DIAS.get(agenda[2]), int(agenda[1]))
                else: print('Dia da semana inválido')
            else: print('Frequência semanal inválida')
        
        elif agenda[0] in ('Mensal', 'Mensalmente', 'mensal', 'mensalmente'):
            if int(agenda[1]) in range(1, 32):
                Sys.addAgenda(1, int(agenda[1]))
            else: print('Dia inválido')
        else: print('Tipo inválido')
        
    def print_payment_schedule(day = time.time()):
            
        current_date = time.localtime(day)
        pending_employees = list()
        print('-'*21)
        print(f'Hoje {time.strftime("%a, %d/%m/%Y", current_date)}')
        print('-'*21)
        print('--SALÁRIOS DEVIDOS--')

        for e in Sys.EmployeeList.values():

            if e.getAgenda(0) == 1:
                if e.getAgenda(1) == current_date.tm_mday:
                    pending_employees.append(e)

            elif e.getAgenda(0) == 2 and e.getAgenda(2) == current_date.tm_wday:
                
                time_diff = time.mktime(current_date) - e.getPayHis(-1, time = True)
                time_diff = time.localtime(time_diff + 1000)
                
                if e.getAgenda(1) == 1 and time_diff.tm_yday in range(6, 8):
                    pending_employees.append(e)
                elif e.getAgenda(1) == 2 and time_diff.tm_yday in range(13, 15):
                    pending_employees.append(e)
                elif e.getAgenda(1) == 3 and time_diff.tm_yday in range(20, 22):
                    pending_employees.append(e)

        for i, e in enumerate(pending_employees):
            print(f'{i}.{e.name}: R${e.accumulated_payment()}/{PAYMETHODS[e.paymethod]}')
        print('-'*21)
        print('1.Pagar salários devidos hoje\n2.Avançar dia\n3.VOLTAR')
        op = input('Escolha uma opção: ')

        if op == '1':
            for e in pending_employees:
                e.pay(time = time.mktime(current_date))

        if op == '2':
            Menu.print_payment_schedule(time.mktime(current_date) + 86400)

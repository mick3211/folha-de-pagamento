from classes.sys import Sys
from classes.employee import Person
import time


ERROR1 = 'FUNCIONÁRIO INVÁLIDO'
ERROR2 = 'SEM FUNCIONÁRIOS CADASTRADOS'
DIAS = {'domingo': 1, 'segunda': 2, 'terça': 3, 'quarta': 4, 'quinta': 5, 'sexta': 6, 'sábado': 7}


class Menu():

    def printData(id, info = True, adress = True):
        if Sys.EmployeeNum > 0:
            current = Sys.isEmployee(id)
            if current != False:

                if info:
                    info_list = current.getInfo()
                    if info_list['type'] == 1: type = "Horista"
                    if info_list['type'] == 2: type = "Assalariado"
                    if info_list['type'] == 3: type = "Comissionado"
                    if info_list['paymethod'] == 1: paymethod = "Cheque pelos Correios"
                    if info_list['paymethod'] == 2: paymethod = "Cheque em mãos"
                    if info_list['paymethod'] == 3: paymethod = "Depósito bancário"
                    print('DADOS:')
                    print('Nome:', info_list['name'])
                    print('CPF:', info_list['cpf'])
                    print('Tipo:', type)
                    print('Método de pagamento:', paymethod)
                    if info_list['syndicate'] != False:
                        print('Pertence ao sindicato')
                        print('Taxa sindical: ', current.syndicate.taxa)
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

    def AddEmployee():
        name = input('Digite o nome do novo empregado: ')
        cpf = input('Insira o CPF: ')

        while cpf in Sys.EmployeeList.keys():
            print('CPF JÁ CADASTRADO, INSIRA NOVAMENTE')
            cpf = input()

        type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: '))
        paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: '))
        adress = list()
        syndicate = True if input('Faz parte do sindicato? [s/n]: ') in 'Ss' else False
        taxa = int(input('Insira o valor da taxa sindical: ')) if syndicate else None
        print('Endereço:')
        adress.append(input('Digite o CEP: '))
        adress.append(int(input('Digite o Número da casa: ')))
        adress.append(input('Digite a rua: '))
        adress.append(input('Digite o bairro: '))
        adress.append(input('Digite a cidade: '))
        adress.append(input('Digite o estado: '))

        Sys.AddEmployee(name, cpf, type, paymethod, adress, syndicate, taxa)
        print('---Novo empregado adicionado:---')
        Menu.printData(cpf)

    def EditEmployee():
        print('--------------')
        if Sys.EmployeeNum > 0:
            id = input('Insira o CPF do empregado a ser editado: ')
            current = Sys.isEmployee(id)
            if current != False:
                Sys.setLastEmployee(id)
                Sys.last_action = 3
                print('EMPREGADO SELECIONADO:')
                Menu.printData(id)

                while True:
                    print('--SELLECIONE UMA OPÇÃO--')
                    print('1.Editar nome\n2.Alterar tipo\n3.Alterar método de pagamento\n4.Editar endereço\n5.Alterar sindicato\n6.Alterar agenda de pagamento\n7.DELETAR\n8.Voltar')
                    option = int(input())
                    if option == 1:
                        current.SetInfo(name = input('Digite o novo nome: '))
                    if option == 2:
                        Sys.setType(id, type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: ')))
                        current = Sys.isEmployee(id)
                    if option == 3:
                        current.SetInfo(paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: ')))
                        
                    if option == 4:
                        while True:
                            print('--SELLECIONE UMA OPÇÃO--')
                            print('1.Alterar CEP\n2.Alterar Rua\n3.Alterar número\n4.Alterar bairro\n5.Alterar cidade\n6.Alterar Estado\n7.Voltar')
                            op = int(input())
                            if op == 1: current.SetAdress(cep = input('Novo CEP: '))
                            if op == 2: current.SetAdress(rua = input('Nova rua: '))
                            if op == 3: current.SetAdress(numero = input('Novo número: '))
                            if op == 4: current.SetAdress(bairro = input('Novo bairro: '))
                            if op == 5: current.SetAdress(cidade = input('Nova cidade: '))
                            if op == 6: current.SetAdress(estado = input('Novo Estado: '))
                            if op == 7: break

                    if option == 5:
                        if current.syndicate != False:
                            print('Funcionário pertence ao sindicato')
                            print('1.Remover do sindicato\n2.Alterar taxa sindical\n3.Voltar')
                            op = int(input('Selecione uma opção: '))
                            if op == 1: current.SetInfo(syndicate = False)
                            if op == 2: current.SetInfo(syndicate = True, taxa = int(input('Insira o novo valor da taxa: ')))
                            if op == 3: pass
                        elif input('Funcionário não pertence ao sindicato, adicionar?[s/n]: ') in 'Ss':
                            current.SetInfo(syndicate = True, taxa = int(input('Insira o valor da taxa: ')))

                    if option == 6:
                        for i, agenda in enumerate(Sys.agendas):
                            if agenda[0] == 1:
                                print(f'{i}.Mensalmente dia {agenda[1]}')
                            if agenda[0] == 2:
                                dia = list(DIAS.keys())
                                print(f'{i}.A cada {agenda[1]} semanas no dia {dia[agenda[2]]}')
                        o = int(input('Selecione a agenda: '))
                        current.SetInfo(agenda = Sys.agendas[o])

                    if option == 7:
                        if input('TEM CERTEZA QUE QUER DELETAR O FUNCIONÁIO? [S/N]: ') in 'Ss':
                            Sys.RemoveEmployee(current.cpf)
                            print('FUNCIONÁRIO DELETADO')
                            return

                    if option == 8: break
                print('--EMPREGADO EDITADO--')
                Menu.printData(id)
            else: print(ERROR1)
        else: print(ERROR2)

    def RegInfo():      
        if Sys.EmployeeNum > 0:
            id = input('Insira o cpf do funcionário: ')
            current = Sys.isEmployee(id)
            if current != False:

                if current.type == 1:
                    if input('Funcionário horista, registrar ponto?[s/n]: ') in 'Ss':
                        if Sys.regPonto(id, time.asctime()):
                            print('Ponto registrado')
                        else: print('Ponto não registrado')

                if current.type == 2: print('Funcionário assalariado')

                if current.type == 3:
                    if input('Funcionário comissionado, lançar nova venda? [s/n]: ') in 'Ss':
                        if Sys.regSale(id, int(input('Insira o valor da venda: '))):
                            print('Venda resgistrada')
                        else: print('Venda não registrada')
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
                
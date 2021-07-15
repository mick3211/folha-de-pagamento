from classes.sys import Sys
from classes.employee import Person
import time


class Menu():
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
        print('Endereço:')
        adress.append(int(input('Digite o CEP: ')))
        adress.append(int(input('Digite o Número da casa: ')))
        adress.append(input('Digite a rua: '))
        adress.append(input('Digite o bairro: '))
        adress.append(input('Digite a cidade: '))
        adress.append(input('Digite o estado: '))

        Sys.AddEmployee(name, cpf, type, paymethod, adress, syndicate)
        print('---Novo empregado adicionado:---')
        Sys.printInfo(cpf)
        print('ENDEREÇO:')
        Sys.printAdress(cpf)

    def EditEmployee():
        print('--------------')
        if Sys.EmployeeNum > 0:
            id = input('Insira o CPF do empregado a ser editado: ')
            current = Sys.SetCurrent(id)
            if current != False:
                print('EMPREGADO SELECIONADO:')
                Sys.printInfo(id)
                Sys.printAdress(id)

                def editAdress():
                    while True:
                        print('--SELLECIONE UMA OPÇÃO--')
                        print('1.Altera CEP\n2.Alterar Rua\n3.Alterar número\n4.Alterar bairro\n5.Alterar cidade\n6.Alterar Estado\n7.Voltar')
                        op = int(input())
                        if op == 1: current.SetAdress(cep = int(input('Novo CEP: ')))
                        if op == 2: current.SetAdress(rua = input('Nova rua: '))
                        if op == 3: current.SetAdress(numero = input('Novo número: '))
                        if op == 4: current.SetAdress(bairro = input('Novo bairro: '))
                        if op == 5: current.SetAdress(cidade = input('Nova cidade: '))
                        if op == 6: current.SetAdress(estado = input('Novo Estado: '))
                        if op == 7: break

                while True:
                    print('--SELLECIONE UMA OPÇÃO--')
                    print('1.Editar nome\n2.Alterar tipo\n3.Alterar método de pagamento\n4.Editar endereço\n5.Alterar sindicato\n6.DELETAR\n7.Voltar')
                    option = int(input())
                    if option == 1:
                        current.SetInfo(name = input('Digite o novo nome: '))
                    if option == 2:
                        current.SetInfo(type = int(input('Escolha o tipo [1.Horista 2.Assalariado 3.Comissionado]: ')))
                    if option == 3:
                        current.SetInfo(paymethod = int(input('Escolha o método de pagamento [1.Cheque pelos Correios 2.Cheque em mãos 3.Depósito bancário: ')))
                    if option == 4: editAdress()
                    if option == 5:
                        if current.syndicate:
                            if input('Funcionário pertence ao sindicato, remover?[s/n]: ') in 'Ss': current.syndicate = False
                        else: 
                            if input('Funcionário não pertence ao sindicato, adicionar?[s/n]: ') in 'Ss': current.syndicate = True
                    if option == 6:
                        if input('TEM CERTEZA QUE QUER DELETAR O FUNCIONÁIO? [S/N]: ') in 'Ss':
                            Sys.RemoveEmployee(current.cpf)
                            print('FUNCIONÁRIO DELETADO')
                            return
                    if option == 7: break

                print('--EMPREGADO EDITADO--')
                current.ShowInfo()
            else: print('FUNCIONÁRIO INVÁLIDO')
        else: print('SEM FUNCIONÁRIOS CADASTRADOS')

    def RegInfo():      
        if Sys.ShowEmployees():
                id = int(input('Selecione o funcionário para registrar informação: '))
                current = Sys.SetCurrent(id)
                if current != False:

                    while True:
                        print('--SELECIONE UMA OPÇÃO--')
                        print('1.Registrar venda\n2.Registrar ponto\n3.Registrar taxa de sindicato\n4.Voltar')
                        option = int(input())
                        
                        if option == 1:
                            value = float(input('Insira o valor: '))
                            current.NewSale(value, time.asctime())
                        if option == 2:
                            current.RegPonto(time.asctime())
                        if option == 3:
                            value = float(input('Insira o valor da taxa: '))
                            current.NovaTaxa(value)
                        if option == 4: break
                else: print('FUNCIONÁRIO INVÁLIDO')
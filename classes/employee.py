import time


SALARY = 2000.00


class Adress():
    def __init__(self):
        self.cep = str()
        self.numero = int()
        self.rua = str()
        self.bairro = str()
        self.cidade = str()
        self.estado = str()


class Syndicate():
    def __init__(self, taxa, id):
        self.syn_tax = taxa
        self.serv_tax = list()
        self.id = id


class Person():
    def __init__(self):
        self.name = str()
        self.cpf = str()
        self.paymethod = int()
        self.adress = Adress()
        self.syndicate = bool()
        self.type = int()
        self.new_agenda = False
        self.pay_his = [{'time': time.time(), 'value': 0}]
        self.next_payday = None

    def SetAdress(self, cep = None, numero = None, rua = None, bairro = None, cidade = None, estado = None):
        if cep: self.adress.cep = cep
        if numero: self.adress.numero = numero
        if rua: self.adress.rua = rua
        if bairro: self.adress.bairro = bairro
        if cidade: self.adress.cidade = cidade
        if estado: self.adress.estado = estado

    def SetInfo(self, name = None, cpf = None, paymethod = None, syndicate = None, taxa = None, agenda = None, salary = None, comissao = None):
        if name: self.name = name
        if cpf: self.cpf = cpf
        if paymethod: self.paymethod = paymethod
        if syndicate != None: 
            if syndicate == False: self.syndicate = False
            else: self.syndicate = Syndicate(taxa, self.cpf)
        if agenda != None: self.new_agenda = agenda
        if salary: self.salary = salary
        if self.type == 3 and comissao: self.comissao = comissao 

    def set_next_payday(self):
        agenda = self.getAgenda()
        c_date = time.localtime()

        if agenda[0] == 1:
            self.next_payday = time.localtime(time.mktime((c_date.tm_year, c_date.tm_mon+1, agenda[1], 12, 0, 0, 0, 0, -1)))
        else:

            self.next_payday = time.localtime(time.mktime((c_date.tm_year, c_date.tm_mon, c_date.tm_mday+7*agenda[1], 12, 0, 0, 0, 0, -1)))

            while self.next_payday.tm_wday > agenda[2]:
                self.next_payday = time.localtime(time.mktime((self.next_payday.tm_year, self.next_payday.tm_mon, self.next_payday.tm_mday-1, 12, 0, 0, 0, 0, -1)))

            while self.next_payday.tm_wday < agenda[2]:
                self.next_payday = time.localtime(time.mktime((self.next_payday.tm_year, self.next_payday.tm_mon, self.next_payday.tm_mday+1, 12, 0, 0, 0, 0, -1)))
        print('Proximo pagamento:',self.next_payday)
   
    def getInfo(self, name = True, cpf = True, paymethod = True, type = True, syndicate = True, salary = True):
        info = {}
        if name: info['name'] =  self.name
        if cpf: info['cpf'] = self.cpf
        if paymethod: info['paymethod'] = self.paymethod
        if salary: info['salary'] = self.salary
        if syndicate:
            if self.syndicate != False:
                info['syndicate'] = True
                info['taxa'] = self.syndicate.syn_tax
            else: info['syndicate'] = False
        if type: info['type'] = self.type
        return info

    def getAdress(self, cep = True, rua = True, numero = True, bairro = True, cidade = True, estado = True):
        adress = {}
        if cep: adress['cep'] = self.adress.cep
        if rua: adress['rua'] = self.adress.rua
        if numero: adress['numero'] = self.adress.numero
        if bairro: adress['bairro'] = self.adress.bairro
        if cidade: adress['cidade'] = self.adress.cidade
        if estado: adress['estado'] = self.adress.estado
        return adress

    def getSynTotal(self):
        if self.syndicate != False:
            return sum(self.syndicate.serv_tax) + self.syndicate.syn_tax
        else: return 0

    def getAgenda(self, i = None):
        if i != None: return self.agenda[i]
        else: return self.agenda

    def getPayHis(self, i = None, time = False):
        if i:
            if time: return self.pay_his[i]['time']
            else: return self.pay_his[i]
        return self.pay_his


class Hourly(Person):
    def __init__(self):
        super().__init__()
        self.type = 1
        self.hisPontos = list()
        self.ini = self.end = None
        self.agenda = (2, 1, 4)
        self.set_next_payday()
        self.salary = float()

    def regPonto(self, date):
        if not self.ini:
            self.ini = date
            return 1
        else:
            self.end: self.end = date
            self.hisPontos.append((int(self.ini), int(self.end)))
            self.ini = self.end = None
            return 2

    def accumulated_payment(self):
        total_h = 0
        total_x = 0
        syn_taxe = self.getSynTotal()

        for i in self.hisPontos:
            worked_h = (i[1] - i[0]) / 3600
            x_work = 0
            if worked_h > 8:
                x_work = worked_h - 8
                worked_h = 8
            total_h += worked_h
            total_x += x_work

        return total_h*self.salary + total_x*self.salary*1.5 - syn_taxe

    def pay(self, time = time.time(), value = float):
        self.hisPontos.clear()
        if self.syndicate != False: self.syndicate.serv_tax.clear()

        if self.new_agenda:
            self.agenda = self.new_agenda
            self.new_agenda = False
            print('Agenda atualizada')

        self.set_next_payday()
        self.pay_his.append({'time': time, 'value': value})
        

class Salaried(Person):
    def __init__(self):
        super().__init__()
        self.type = 2
        self.agenda = (1, 30)
        self.set_next_payday()
        self.salary = float()

    def accumulated_payment(self):
        syn_taxe = self.getSynTotal()

        if self.agenda[0] == 1: return self.salary - syn_taxe
        else: return (self.salary/4)*self.agenda[1] - syn_taxe

    def pay(self, time = time.time(), value = float):          
        if self.syndicate != False: self.syndicate.serv_tax.clear()

        if self.new_agenda:
            self.agenda = self.new_agenda
            self.new_agenda = False
            print('Agenda atualizada')

        self.set_next_payday()
        self.pay_his.append({'time': time, 'value': value})


class Commissioned(Person):
    def __init__(self):
        super().__init__()
        self.type = 3
        self.hisVendas = dict()
        self.agenda = (2, 2, 4)
        self.set_next_payday()
        self.salary = float()
        self.comissao = float()

    def regSale(self, sale, date):
        self.hisVendas.update({date: sale})

    def accumulated_payment(self):
        syn_taxe = self.getSynTotal()
        if self.agenda[0] == 2:
            return (self.salary/4)*self.agenda[1] + sum(self.hisVendas.values())*self.comissao - syn_taxe
        else: return self.salary + sum(self.hisVendas.values())*self.comissao - syn_taxe

    def pay(self, time = time.time(), value = float):
        self.hisVendas.clear()             
        if self.syndicate != False: self.syndicate.serv_tax.clear()

        if self.new_agenda:
            self.agenda = self.new_agenda
            self.new_agenda = False
            print('Agenda atualizada')

        self.set_next_payday()
        self.pay_his.append({'time': time, 'value': value})

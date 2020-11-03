from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data = date.today()
    #print(data.strftime('%d/%m/%y')) dia e mes como numero
    print(data.strftime('%A %B %Y'))

def trabalhando_com_time():
    hora = time(hour=15, minute=18, second=30)
    print(hora.strftime('%H:%M:%S')) #deixa como string

def trabalhando_com_datetime():
    data = datetime.now()
    print(data)
    print(data.strftime('%d/%m/%y'))
    print(data.strftime('%c'))
    print(data.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    data_string = '01/01/2018'
    data_conv = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_conv)

    nova = data_conv - timedelta(days=365)
    print(nova)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
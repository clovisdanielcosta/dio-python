from datetime import date, time, datetime, timedelta

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    print(data_atual.month)
    print(data_atual.day)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.second)
    print(data_atual.date())
    print(data_atual.weekday())

    # Trazendo o dia da semana em texto traduzido
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    # Criando uma data
    data_criada = datetime(2020, 6, 26, 4, 16, 53)
    print(data_criada)
    print(data_criada.strftime('%c'))

    # Convertendo uma String de Data em Date
    data_string = '15/06/2020 12:20:15'
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(data_convertida.weekday())
    print(data_convertida.day)

    # Somando e subtraindo datas e horário
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

    nova_data2 = data_convertida - timedelta(minutes=12)
    print(nova_data2)

def trabalhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%d-%m-%Y'))
    print(data_atual.strftime('%d %m %Y'))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_time():
    horario = time(hour=15, minute=20, second=50)
    print(horario)

if __name__ == '__main__':
    #trabalhando_date()
    #trabalhando_time()
    trabalhando_datetime()
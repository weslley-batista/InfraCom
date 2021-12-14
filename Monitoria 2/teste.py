"""import datetime
time_1 = datetime.timedelta(hours= 0 , minutes=0, seconds=0)
time_2 = datetime.timedelta(hours= 0, minutes=0, seconds=20)
time_Count = datetime.timedelta(hours= 0, minutes=0, seconds=1)"""

"""from threading import Timer

def hello():
    print ("variavel negativa")
    Timer(30.0, hello).start()

Timer(30.0, hello).start()"""

"""import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')"""




"""import datetime
a = datetime.datetime.now();
print((a.hour,a.minute, a.second))

horaInicial = a.second
#horaAjustada = horaInicial + datetime.timedelta(seconds = 20);
print (horaInicial)"""

"""import datetime as dt

print(dt.datetime.now())

agora = dt.datetime.now();
daqui_um_segundo = agora + dt.timedelta(seconds = 20);
daqui_um_minuto = agora + dt.timedelta(minutes = 1);
daqui_uma_hora = agora + dt.timedelta(hours = 1);

#agora1 = agora.strftime("%Y-%m-%d %H:%M:%S")
agora2 = agora.strftime("%H:%M:%S")
depois = daqui_um_segundo.strftime("%H:%M:%S")
#agora3 = agora.strftime("%S")


print(agora2)
print(depois)"""
#print(daqui_uma_hora)


"""from datetime import datetime
from dateutil.relativedelta import relativedelta

a = "2015-08-05 08:12:23"
b = "2015-08-09 08:12:23"
f = "%Y-%m-%d %H:%M:%S"

ini = datetime.strptime(a, f)
fim = datetime.strptime(b, f)

di = abs(relativedelta(ini, fim))

print(f'{di.years} anos, {di.months} meses, {di.days} dias, {di.hours} horas, '
      f'{di.minutes} minutos e {di.seconds} segundos.')"""


"""#timer
from threading import Timer
def false():
  print("teste")
 
t = Timer(5.0, false)
t.start()"""

"""
data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)"""
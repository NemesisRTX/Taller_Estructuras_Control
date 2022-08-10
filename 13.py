#Librerias
from datetime import date
#Día actual
today = date.today()
#Fecha actual
dia_a=today.day
mes_a=today.month
año_a=today.year
#Entradas
f_nacimiento=input("Ingrese fecha de nacimiento (use el formato año/mes/dia): ")
(año,mes,dia)=f_nacimiento.split("/")
año_n=int(año)
mes_n=int(mes)
dia_n=int(dia)
#Caja Negra
edad=0
if(mes_a==mes_n):
    if(dia_n>=dia_a):
        edad=(año_a-año_n)-1
    else:
        edad=(año_a-año_n)
elif(mes_a>mes_n):
    edad=(año_a-año_n)
else:
    edad=(año_a-año_n)-1
#--------------------------//Signos\\--------------------------
if((dia_n>=22 and mes_n>=11) or (dia_n<=21 and mes_n<=12)):
    signo="Sagitario"
if((dia_n>=22 and mes_n>=12) or (dia_n<=20 and mes_n<=1)):
    signo="Capricornio"
if((dia_n>=21 and mes_n>=1) or (dia_n<=19 and mes_n<=2)):
    signo="Acuario"
if((dia_n>=20 and mes_n>=2) or (dia_n<=19 and mes_n<=3)):
    signo="Piscis"
if((dia_n>=21 and mes_n>=3) or (dia_n<=20 and mes_n<=4)):
    signo="Aries"
if((dia_n>=21 and mes_n>=4) or (dia_n<=21 and mes_n<=5)):
    signo="Tauro"
if((dia_n>=22 and mes_n>=5) or (dia_n<=21 and mes_n<=6)):
    signo="Geminis"
if((dia_n>=22 and mes_n>=6) or (dia_n<=22 and mes_n<=7)):
    signo="Cancer"
if((dia_n>=23 and mes_n>=7) or (dia_n<=23 and mes_n<=8)):
    signo="Leo"
if((dia_n>=24 and mes_n>=8) or (dia_n<=22 and mes_n<=9)):
    signo="Virgo"
if((dia_n>=23 and mes_n>=9) or (dia_n<=22 and mes_n<=10)):
    signo="Libra"
if((dia_n>=23 and mes_n>=10) or (dia_n<=21 and mes_n<=11)):
    signo="Escorpion"
else:
    signo="Entrada"
#Salidas
print(edad)
print(signo)

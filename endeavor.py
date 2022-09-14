
from  datetime import  date
import datetime

garantia = "Carro"
cantidad = 5000
dias = 30
taza = 0
fechaX = date.today()

if dias == 15 and cantidad >= 200:
    taza = 20
    fechaY = fechaX + datetime.timedelta(dias)

elif dias == 30 and cantidad >= 1000:
    taza = 30
    fechaY = fechaX + datetime.timedelta(dias)



interes = taza/100
redito = cantidad * interes
total = redito + cantidad


factura =  "Garantia : " + " " + garantia + "\n" + "Cantidad : " + str(cantidad) + "\n" + "Dias : " + str(
    dias)+ "\n" + "Fecha X : " + str(fechaX.strftime("%Y-%m-%d")) + "\n" + "Taza : " + str(taza) + "%" + "\n" + "Redito : " + str(redito) + "\n" + "Total : " + str(total) + "\n" +  "Fecha Y : " + str(fechaY.strftime("%Y-%m-%d"))


print(factura)

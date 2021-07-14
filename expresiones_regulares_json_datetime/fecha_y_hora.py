print("*********************************************")
print("                 Datetime                    ")
print("*********************************************")

# Importar clase datetime desde el modulo datetime
from datetime import datetime

fechayhora = datetime.now()
print(fechayhora)

anio = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print(f"La hora es {hora}:{minutos}:{segundos}")
print(f"y es el día {dia} del mes {mes} del año {anio}")

import datetime

def mostrar_fecha():
    hoy = datetime.date.today()  
    print("La fecha de hoy es:", hoy.day, "/", hoy.month, "/", hoy.year)



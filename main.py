# main.py

from fecha import mostrar_fecha
from saludar import saludar

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Saludar")
        print("2. Mostrar fecha")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            saludar()
        elif opcion == "2":
            mostrar_fecha()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()

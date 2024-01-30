import mysql.connector

def menu():
    print("Programa agenda")
    print("Selecciona una opcion")
    print("1.-inserta un registro")
    print("2.-Listado de registros")
    print("3.-Actualizar un registro")
    print("4.-Eliminar un registro")
    opcion = input("opcion: ")
    if opcion == "1":
        print("Insertamos un registro")
    elif opcion == "2":
        print("Listamos registros")
    elif opcion == "3":
        print("Actualizamos un registro")
    elif opcion == "4":
        print("Eliminamos un registro")
menu()

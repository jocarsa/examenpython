import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="examenpython",
    password="examenpython",
    database="examenpython",
    )
cursor = conexion.cursor()

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
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        direccion = input("Introduce la direccion: ")
        telefono = input("Introduce el telefono: ")
        email =  input("Introduce el email: ")
        peticion = "INSERT INTO clientes VALUES (NULL,'"+nombre+"','"+apellidos+"','"+direccion+"','"+telefono+"','"+email+"')"
        cursor.execute(peticion)
        conexion.commit()
    elif opcion == "2":
        print("Listamos registros")
        peticion = "SELECT * FROM clientes"
        cursor.execute(peticion)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    elif opcion == "3":
        print("Actualizamos un registro")
    elif opcion == "4":
        print("Eliminamos un registro")
    menu()
menu()

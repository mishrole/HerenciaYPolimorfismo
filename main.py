from Persona import Persona

print("***** MENU *****")
print("1. Agregar una persona")
print("2. Mostrar lista de personas")
print("3. Terminar el programa")

opcion = input("Opción a elegir: ")

while opcion != "3":
    if opcion == "1":
        nombre = input("Dame el nombre de la persona: ")
        apellido = input("Dame el apellido de la persona: ")
        nuevaPersona = Persona(nombre, apellido)
    elif opcion == "2":
        print("Mostrando la lista de personas")
        Persona.imprimeListaPersonas()
    else:
        print("Opción incorrecta")
    
    print("***** MENU *****")
    print("1. Agregar una persona")
    print("2. Mostrar lista de personas")
    print("3. Terminar el programa")

    opcion = input("Opción a elegir: ")
        
    
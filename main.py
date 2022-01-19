from Persona import Persona
from Estudiante import Estudiante

# alex = Estudiante("Alex", "Martinez", 132456, "Fundamentos de la web")
# alex.informacion()
# alex.asignaCalificacion(8.9)
# alex.informacion() # Hereda del padre y sóo tiene nombre y apellido
# Pero podemos crear un nuevo método o sobreescribir el método del padre

print("***** MENU *****")
print("1. Agregar una persona")
print("2. Mostrar lista de personas")
print("3. Agregar un estudiante")
print("4. Mostrar lista de estudiantes")
print("5. Terminar el programa")

opcion = input("Opción a elegir: ")

while opcion != "5":
    if opcion == "1":
        nombre = input("Dame el nombre de la persona: ")
        apellido = input("Dame el apellido de la persona: ")
        nuevaPersona = Persona(nombre, apellido)
    elif opcion == "2":
        print("Mostrando la lista de personas")
        Persona.imprimeListaPersonas()
    elif opcion == "3":
        nombre = input("Dame el nombre del estudiante: ")
        apellido = input("Dame el apellido del estudiante: ")
        id = input("Dame el id del estudiante: ")
        curso = input("Dame el curso del estudiante: ")
        nuevoEstudiante = Estudiante(nombre, apellido, int(id), curso)
    elif opcion == "4":
        print("Mostrando la lista de estudiantes")
        Estudiante.imprimeListaEstudiantes()
    else:
        print("Opción incorrecta")
    
    print("***** MENU *****")
    print("1. Agregar una persona")
    print("2. Mostrar lista de personas")
    print("3. Agregar un estudiante")
    print("4. Mostrar lista de estudiantes")
    print("5. Terminar el programa")

    opcion = input("Opción a elegir: ")
        
    
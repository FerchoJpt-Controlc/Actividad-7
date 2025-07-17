estudiantes={}

def RegistrarEstudiante():
    cantidad=int(input("\ningrese cuantos estudiantes decea ingresar: "))

    for i in range(cantidad):
        carnet=input("\ningrese carnet del estudiante: ")
        nombre=input("\ningrese nombre del estudiante: ")
        edad=input("\ningrese edad del estudiante: ")
        carrera=input("\ningrese carrera del estudiante: ")

        cursos={}
        numCursos=int(input("\ningrese cuantos cursos desea registrar: "))
        for i in range(numCursos):
            nomCurso=input("\ningrese la clave del curso: ")
            notaTarea=float(input("\ningrese nota tarea: "))
            notaParcial=float(input("\ningrese nota parcial: "))
            notaProyecto=float(input("\ningrese nota proyecto: "))

            cursos[nomCurso]={
                "notaTarea":notaTarea,
                "notaParcial":notaParcial,
                "notaProyecto":notaProyecto,

            }

        estudiantes[carnet]={
            "nombre":nombre,
            "edad":edad,
            "carrera":carrera,
            "cursos":cursos,
        }

def BuscarEstudiante():
    print("\nBúsqueda de estudiante")
    buscado = input("Ingrese el número de carnet que desea buscar: ")

    if buscado in estudiantes:
        estudiante = estudiantes[buscado]
        print("\nEstudiante encontrado:")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Carrera: {estudiante['carrera']}")

    else:
        print("\nEstudiante no encontrado.")


def Menu():
    while True:
        print("\nM E N U")
        print("\n1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar por carnet")
        print("4. salir")
        opcion=int(input("\ningrese una opcion: "))
        if opcion==1:
            RegistrarEstudiante()
       # elif opcion==2:
        elif opcion==3:
            BuscarEstudiante()
        elif opcion==4:
            print("gracias por usaar el sistemka ")
            break
        else:
            print("opcion no valida")

Menu()



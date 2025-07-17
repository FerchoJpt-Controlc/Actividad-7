estudiantes={}

def RegistrarEstudiante():
    cantidad=int(input("ingrese cuantos estudiantes decea ingresar: "))

    for i in range(cantidad):
        carnet=input("ingrese carnet del estudiante: ")
        nombre=input("ingrese nombre del estudiante: ")
        edad=input("ingrese edad del estudiante: ")
        carrera=input("ingrese carrera del estudiante: ")

        cursos={}
        numCursos=int(input("ingrese cuantos cursos desea registrar: "))
        for i in range(numCursos):
            nomCurso=input("ingrese la clave del curso: ")
            notaTarea=float(input("ingrese nota tarea: "))
            notaParcial=float(input("ingrese nota parcial: "))
            notaProyecto=float(input("ingrese nota proyecto: "))

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

def MostrarEstudiantes():


def Menu():
    while True:
        print("\nM E N U")
        print("\n1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar por carnet")
        print("4. salir")
        opcion=int(input("ingrese una opcion: "))
        if opcion==1:
            RegistrarEstudiante()
       # elif opcion==2:
       # elif opcion==3:
        elif opcion==4:
            print("gracias por usaar el sistemka ")
            break
        else:
            print("opcion no valida")

Menu()



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
            nomCurso=input("ingrese nomcurso del curso: ")
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


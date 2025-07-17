#SISTEMA ADMINISTRACIÓN ESTUDIANTES.
estudiantes=[]

while True:
    print("---Menú de Registro de Estudiantes---")
    print("1.Agregar Estudiante.\n 2.Eliminar Estudiante.\n 3.Mostrar Estudiantes\n 4.Salir")
    opcion=input("Seleccione una opción:")

    if opción=="1":
        estudiante_agregar= input("Ingrese el nombre de estudiante a agregar:")
        estudiantes.append(estudiante_agregar)
        print(f"{estudiante_agregar} agregado exitosamente!")






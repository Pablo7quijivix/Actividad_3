#SISTEMA ADMINISTRACIÓN ESTUDIANTES.
estudiantes=[]

while True:
    print("---Menú de Registro de Estudiantes---")
    print("1.Agregar Estudiante.\n 2.Eliminar Estudiante.\n 3.Mostrar Estudiantes\n 4.Salir")
    opcion=input("Seleccione una opción:")

    if opcion=="1":
        estudiante_agregar= input("Ingrese el nombre de estudiante a agregar:")
        estudiantes.append(estudiante_agregar)
        print(f"{estudiante_agregar} agregado exitosamente!")

    if opcion =="2":
        estudiante_eliminar=input("Ingrese nombre de estudiante a eliminar:")
        if estudiante_eliminar in estudiantes:
            estudiantes.remove(estudiante_eliminar)
        print(f"{estudiante_eliminar} eliminado Exitosamente!")

    if opcion =="3":
        for student in range(len(estudiantes)):
            print(f"estudiante no.{student+1}__{estudiantes[student]}")

    if opcion =="4":
        print(f"___Saliendo del sistema.........")
        break





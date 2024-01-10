import json
import os
import jSonFun

students = {}
identification = None
__all__ = ["students", "identification"]

def searchStudent(students):
    identification = input("Ingrese el número de documento: ")
    if identification in students:
        print(students)
        return identification
    else:
        print("El documento ingresado no está registrado.")
        while True:
            opcion = int(input((f"¿Desea registrar el documento: {identification}?\n\t1. Sí.\n\t2. No.\n")))
            if opcion == 1:
                registerStudent(students, identification)
                break
            elif opcion == 2:
                break
            else:
                print("Debe ingresar 1 o 2.")
    return identification

def registerStudent(students, identification):
    while True:
        print("-----------------Registro de estudiantes--------------------")
        student = {}
        print(identification)
        if len(str(identification)) == 0 or identification is None or identification == 0:
            try:
                identification = input("Ingrese el número de documento: ")
            except ValueError:
                print("Error: Ingrese un valor válido para el número de documento.")
                continue

        else:
            if identification in students:
                print(f"El documento {identification} ya se encuentra registrado con el estudiante {students[identification].get('full_name', 'No hay datos del estudiante')}")
            else:
                try:
                    name = input("Ingrese nombre completo del estudiante: ")
                    age = int(input("Ingrese la edad del estudiante: "))
                    if age < 0:
                        print("La edad no puede ser negativa.")
                        continue

                    student['id'] = identification
                    student['full_name'] = name
                    student['age'] = age
                    students[identification] = student
                    jSonFun.toJSON(students, 'students')
                    option = int(input("¿Desea registrar otro estudiante?\n\t1. Si\n\t2. No.\n"))

                    if option == 2:
                        break

                    elif option != 1:
                        print("Debe elegir entre 1 o 2.")

                except ValueError:
                    print("Error: Ingrese un valor válido para la edad.")

    return students





if __name__ == "__main__":
    print("----------------MODULO STUDENT-------------------------------")
    while True:
        print("-----------------Menu Principal-------------")
        option = int(input("\t1. Registrar estudiante.\n\t2. Busca estudiante.\n\t3. Listar estudiantes.\n"))
        if option == 1:
            students = registerStudent(students, identification= 0)
        elif option == 2:
            searchStudent(students)
        elif option == 3:
            print(students)
        elif option == 0:
            break

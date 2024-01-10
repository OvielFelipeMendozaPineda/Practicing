import os
import json
import jSonFun
import student
from student import students, identification

def menuPrincipal(students, identification):
    while True:
        print("-----------------Menu Principal-------------")
        option = int(input("\t1. Registrar estudiante.\n\t2. Busca estudiante.\n\t3. Listar estudiantes.\n"))
        if option == 1:
            students = student.registerStudent(students, identification= 0)
        elif option == 2:
            student.searchStudent(students)
        elif option == 3:
            print(students)
        elif option == 0:
            break



menuPrincipal(students, identification)
class Student:
    def __init__(self):
        self.name = ["Felipe", "Luna"]
        self.age = [12, 14]
        self.grades = [6, 7, 8]

    def add_grade(self):
        numero = int(input("Ingrese el grado del estudiante: "))
        self.grades.append(numero)

    def average_grade(self):



estudiante = Student()
print(estudiante.add_grade())
print(estudiante.grades)


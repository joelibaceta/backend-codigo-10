# Usar POO para escribir una aplicación 
# que permita registrar notas de los alumnos 
# y obtener su promedio, las notas debe ser privadas.

class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.__notas = []

    def registrar_nota(self, nota):
        self.__notas.append(nota)

    def get_promedio(self):
        total = 0
        cantidad = len(self.__notas)
        for nota in self.__notas:
            total = total + nota
        return total / cantidad
        
class Curso:

    def __init__(self):
        self.alumnos = []

matematica = Curso()

alumno1 = Alumno("Diana")
alumno1.registrar_nota(12)
alumno1.registrar_nota(15)
alumno1.registrar_nota(18)

matematica.alumnos.append(alumno1)

for alumno in matematica.alumnos:
    print(f"Promedio {alumno.nombre}: {alumno.get_promedio()}")

class Empleado:

    def __init__(self, nombre, dni, salario=980):
        self.nombre = nombre
        self.__salario = salario
        self.__dni = dni

    def setSalario(self, monto):
        if monto >= 980:
            self.__salario = monto
        else:
            raise Exception("Minimo sueldo permitido: 980")

    def __getSalario(self):
        """Obtiene el salario final [metodo privado]"""
        salario_base = self.__salario
        return salario_base * 0.89

    def pagar(self):
        salario_final = self.__getSalario()
        print("salario pagado!")

    def print_dni(self):
        return self.__dni

empleado1 = Empleado("Juan", 12312434, 2000)
empleado2 = Empleado("Diego", 8723212)

empleado2.setSalario(1500)



print(empleado1.nombre)
#print(empleado1.__salario)
print(empleado1.print_dni())

print(empleado1._Empleado__salario)

print(dir(empleado1))
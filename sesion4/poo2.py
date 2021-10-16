class Empleado:
    def __init__(self, nombre, apellido, salario, dni):
        self.nombre = nombre 
        self.apellido = apellido
        self.salario = salario
        self.dni = dni
    
    def reportar(self):
        print(f"{self.nombre} reporto")

class Vendedor(Empleado):
    
    def vender(self):
        print(f"{self.nombre} vendio")

vendedor1 = Vendedor("Marta", "Gutierrez", 2000, 12931283)
vendedor2 = Vendedor("Juan", "Perez", 2000, 21342344)
vendedor1.vender()
vendedor1.reportar()

class Contador(Empleado):
    def __init__(self, nombre, apellido, salario, dni, cod_colegiatura):
        super().__init__(nombre, apellido, salario, dni)
        self.cod_colegiatura = cod_colegiatura

    def declarar_impuestos(self):
        print(f"{self.nombre} declaro impuestos")

contador1 = Contador("Pedro", "Rivera", 5000, 12312443, 324234)
contador1.declarar_impuestos()
contador1.reportar()
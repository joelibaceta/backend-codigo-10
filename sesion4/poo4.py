class Asiento():
    def __init__(self, color="negro"):
        self.color = color

class Car():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class StandardCar(Car):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.asientos = [Asiento(), Asiento(), Asiento(), Asiento()]
        self.tipo = "Mecanico"

class Convertible(Car):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.asientos = [Asiento(), Asiento()]

class CustomCar(Car):
    def __init__(self, marca, modelo, asientos):
        super().__init__(marca, modelo)
        self.asientos = asientos
    


honda_civic = StandardCar(marca="Honda", modelo="Civic")

honda_civic.asientos[0].color = "rojo"

for asiento in honda_civic.asientos:
    print(asiento.color)

ferrari = Convertible(marca="lamborghini", modelo="aventador")

asiento1 = Asiento("Rojo")
asiento2 = Asiento("Azul")
asiento3 = Asiento("Verde")

asientos = [asiento1, asiento2, asiento3]

micarro = CustomCar("Subaru", "X1", asientos)

for asiento in micarro.asientos:
    print(asiento.color)
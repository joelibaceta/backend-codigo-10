# Escriba una aplicación usando POO que nos permita registrar 
# informacion de diferentes tipos de vehiculos 
# ( Autos, Camionetas y Motocicletas ) 
# enfocandonos en la reutilizacion del codigo.

class Vehiculo():
    def __init__(self, placa):
        self.placa = placa

class Auto(Vehiculo):
    def __init__(self, placa, ocupantes=5, asientos=5):
        super().__init__(placa)
        self.ocupantes = ocupantes
        self.asientos = asientos

class Camioneta(Auto):
    def __init__(self, placa, ocupantes=5, asientos=5, traccion):
        super().__init__(placa, ocupantes, asientos)
        self.traccion = traccion
        
class Motocicleta(Vehiculo):
    pass


class Persona:

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
    
    def print_dni(self):
        print(super().__getattribute__("dni"))

    def __getattribute__(self, attr):
        print(f"Atributo {attr} solicitado")
        if attr == "dni":
            return "*******"
        else:
            return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        print(f"Se asigna el valor de {value} a {attr}")
        if attr == "dni":
            if len(str(value)) == 8:
                super().__setattr__(attr, value)
            else:
                raise Exception("DNI debe tener 8 digitos")
        else:
            super().__setattr__(attr, value)

persona1 = Persona("Dora", 78687656)

print(persona1.nombre)

print(persona1.dni)

persona1.print_dni()

persona1.dni = 23412341

persona1.print_dni()
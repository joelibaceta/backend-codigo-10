
def saludar(nombre):
    """Esta funcion saluda"""
    return f"Hola, {nombre}!"

saludo = saludar("Juan")
print(saludo)

saludo = saludar("Mariana")
print(saludo)

def despedirse():
    print("Bye!")

despedirse()


saludar(nombre="Juliana")


def buscar(nombre, fechanac, nacionalidad):
    # buscar
    return f"lo encontre!, {nombre}"

buscar(fechanac="12/04/1987", nombre="Juan", nacionalidad="Mexico")
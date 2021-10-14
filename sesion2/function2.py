
def saludar(name):
    return f"Hola, {name}!"

saludo = saludar("Pedro")

print(saludo)


def saludar(nombre, palabra="Hola", esdespedida=False):
    if esdespedida:
        return "Bye"
    else:
        return f"{palabra}, {nombre}!"

saludo = saludar("Pedro")
print(saludo)

saludo = saludar("Charles", "Hello")
print(saludo)

saludo = saludar("Charlotte", esdespedida = True)
print(saludo)


def functionextrana(attr1, *args, **kwargs):
    return "hice algo"

functionextrana(1, 2, 3, option1=2, option2=3, option3=4)

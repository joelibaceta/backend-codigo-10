edad = input("ingresa tu edad : ")

n = int(edad)

if n >= 18:
    print("es mayor de edad")
elif n < 0:
    print("edad invalida")
else:
    print("es menor de edad")
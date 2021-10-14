# 1. Sumar primer y ultimo elemento
# 2. Asignar el valor 3 al cuarto elemento
# 3. Sumar todos los elementos de la coleccion 

#       0  1  2  3   4  5
col1 = [1, 3, 9, 12, 8, 7]

suma_primero_ultimo = col1[0] + col1[-1]

print(col1)


col1[4] = 3 # [1, 3, 9, 12, 3, 7]

print(col1)

suma = 0
for i in range(0, 6): # i: 0, 1, 2, 3, 4, 5
    suma = suma + col1[i]

suma = 0
for x in col1:
    suma = suma + x


col1[6] = 11
# 1. Sumar todos los elementos numericos
# 2. Sumar los elementos y si hay un 
#    entero como literal convertirlo y sumarlo

col2 = [3, 5, 8, 9, 13, "4"]

suma = 0

for x in col2:
    if type(x) == int:
        suma = suma + x

for x in col2:
    if type(x) == int:
        suma = suma + x
    else:
        x_convertida = int(x)
        suma = suma + x_convertida

# Sumar todos los elementos si hay un literal convertirlo

col2 = [3, 5, 8.3, 9, 13, "4"]

for x in col2:
    if type(x) == int or type(x) == float:
        suma = suma + x
    else:
        x_convertida = int(x)
        suma = suma + x_convertida


col2 = [3, 5, 8.3, 9, 13, "4", "hello"]

for x in col2:
    if type(x) == int or type(x) == float:
        suma = suma + x
    elif x.isnumeric():
        x_convertida = int(x)
        suma = suma + x_convertida
        
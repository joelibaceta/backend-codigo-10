# Escribir una funcion que retorna verdadero 
# si la palabra ingresada como parametro es palindroma.

# ABBA => True
# ABCDDA => False

def invertir(palabra):
    """Esta funcion invierte un texto"""
    tamano = len(palabra)
    nueva_palabra = ""
    for i in range( 1, ( tamano + 1 ) ):
        nueva_palabra = nueva_palabra + palabra[-i]
    return nueva_palabra

def espalindromo(palabra):
    palabra_invertida = invertir(palabra)

    if palabra_invertida == palabra:
        return True
    else:
        return False


def espalindromo2(palabra):

    longitud = len(palabra)

    for in range(0, longitud):
        if (palabra[i] != palabra[-(i+1)])
            return False
    return True
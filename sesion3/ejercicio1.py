# Escribir una funcion que recibe un texto 
# y retorna el texto invertido.

# “hello world” => “dlrow olleh”

# >>> a = "hello"
# >>> list(a)
# ['h', 'e', 'l', 'l', 'o']


def invertir(palabra):
    """Esta funcion invierte un texto"""

    tamano = len(palabra)

    nueva_palabra = ""

    for i in range( 1, ( tamano + 1 ) ):
        nueva_palabra = nueva_palabra + palabra[-i]

    return nueva_palabra

def invertir2(palabra):

    tamano = len(palabra)
    
    nueva_palabra_col = []

    for i in range(1, ( tamano + 1 )):
        nueva_palabra_col.append(palabra[-i])

    return "".join(nueva_palabra_col)

resultado = invertir("hello world")
print(resultado)

resultado2 = invertir2("hello world")
print(resultado2)
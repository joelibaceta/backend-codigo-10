from PIL import Image
from PIL import ImageEnhance

imagen_gato = Image.open("gato.png")

#imagen_rotada = imagen_gato.rotate(45)

#imagen_rotada.save("gato.bmp")

#imagen_gato.thumbnail((150, 150))

mejorador = ImageEnhance.Contrast(imagen_gato)
mejorador.enhance(1.9).show("30% more contrast")


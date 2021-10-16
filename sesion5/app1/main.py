
from lib.converter import Converter
from lib.parser import pedir_centigrados

degrees = pedir_centigrados()
result = Converter.ctof(degrees)
print(f"Farenheit : {result}")
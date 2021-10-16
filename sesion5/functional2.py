import functools

a = [12, 11, 21, 8, 10, 5, 22]

def aprobado(nota):
    return nota < 10

def aprobar(nota):
    return nota + 5

result = list(filter(aprobado, a))
result2 = map(aprobar, result)

print(list(result))
print(list(result2))

print(list(map(lambda y: y+5, list(filter(lambda x: x<10, a)))))

total=0
for i in a:
    total=total+i

result3 = functools.reduce(lambda x, y: x+y, a)
print(result3)

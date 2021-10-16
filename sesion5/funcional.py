
a = ["1", "8", "9", "10", "11"]

nuevo_a = []
for i in a:
    nuevo_a.append(int(i))

print(nuevo_a)


def convertir(i):
    return int(i)
result = map(convertir, a)
print(list(result))

print(list(map(lambda x: int(x), a)))



# 

col2 = map(lambda x: int(x), a)
col3 = map(lambda y: y*2, col2)
print(list(col3))

print(list(map(lambda y: y*2, map(lambda x: int(x), a))))


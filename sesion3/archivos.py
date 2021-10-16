import random

f = open("prueba.txt", "r")

l = f.readline()
print(l)

for i in range(0, 10):
    r1 = f.read(i)
    print(r1)


print(f.read())

f.close()

f = open("output.txt", "w")

for i in range(0,10):
    aleatorio = str(random.random())
    f.write(f"{aleatorio}\n")

f.close()

f = open("output.txt", "a")

for i in range(0,5):
    aleatorio = str(random.random())
    f.write(f"{aleatorio}\n")

f.close()

col = ["4.23423\n", "1.123123\n", "8.1231233\n", "9.123233\n"]

f = open("output.txt", "a")
f.writelines(col)

f.close()
class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def dormir(self):
        print("zZzZ")

    def mover(self):
        print("caminar")

class Sponge(Animal):
    def mover(self):
        pass

class Cat(Animal):
    def hacer_ruido(self):
        print("Meow")

class Fish(Animal):
    def mover(self):
        print("swim")
    
    def hacer_ruido(self):
        print("glu glu")

pelusa = Cat("Pelusa")
pelusa.dormir()
pelusa.mover()
pelusa.hacer_ruido()

nemo = Fish("Nemo")
nemo.dormir()
nemo.mover()
nemo.hacer_ruido()

bob = Sponge("Bob")
bob.dormir()
bob.mover()

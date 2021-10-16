
class Item():
    def __init__(self, nombre, price):
        self.nombre = nombre
        self.price = price
        self.cantidad = 1

    def aumentar(self):
        self.cantidad = self.cantidad + 1

    def disminuir(self):
        self.cantidad = self.cantidad - 1

    def total(self):
        return self.cantidad * self.price

    def __str__(self):
        return f"{self.nombre}\t\t{self.price}\t{self.cantidad}\t{ self.total() } "

class Producto(Item):

    def __init__(self, nombre, price, sku):
        super().__init__(nombre, price)
        self.sku = sku

class Servicio(Item):
    def aumentar(self):
        pass

    def disminuir(self):
        pass

class Carrito():

    def __init__(self):
        self.lista = []

    def pagar(self, metodo_pago):
        print(f"{self.calcular_total()} pagado con {metodo_pago}")

    def calcular_total(self):
        total = 0
        for item in self.lista:
            total = total + item.total()
        return total


carrito1 = Carrito()

item_silla          = Producto(nombre = "Silla Tiziani",         price=780.0, sku="0001")
item_cocina         = Producto(nombre = "Cocia Mabe",            price=580.0, sku="0002")
item_instalacion    = Servicio(nombre = "Instalacion de cocina", price=20.0)

item_silla.aumentar()
item_silla.aumentar()
item_cocina.aumentar()
item_instalacion.aumentar()

carrito1.lista = [item_silla, item_cocina, item_instalacion]

for item in carrito1.lista:
    print(item)

carrito1.pagar("visa")


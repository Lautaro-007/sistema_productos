from producto import Producto


class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, "Electrónico", precio, stock)
        self.garantia_meses = garantia_meses

    def mostrar_garantia(self):
        print("Garantía:", self.garantia_meses, "meses")

    def calcular_precio_final(self):
        # recargo del 5 %.
        return self.precio * 1.05

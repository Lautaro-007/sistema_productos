from producto import Producto


class Alimento(Producto):
    def __init__(self, nombre, precio, stock, vencimiento):
        super().__init__(nombre, "Alimento", precio, stock)
        self.vencimiento = vencimiento

    def mostrar_vencimiento(self):
        print("Fecha de vencimiento:", self.vencimiento)

    def calcular_precio_final(self):
        # descuento del 10 %.
        return self.precio * 0.90

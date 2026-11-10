class Producto:
    def __init__(self, nombre, tipo, precio, stock):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

       
        self.__stock = 0
        self.set_stock(stock)

    def get_stock(self):
        # Getter: devuelve el stock actual.
        return self.__stock

    def set_stock(self, nuevo_stock):
        # Setter: cambia el stock solo si el valor es válido.
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock inválido: no puede ser negativo.")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print("Venta realizada correctamente.")
        else:
            print("Stock insuficiente.")

    def reponer(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a reponer debe ser mayor que cero.")
        else:
            self.__stock += cantidad
            print("Reposición realizada correctamente.")

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo)
        print("Precio original: $", self.precio)
        print("Stock:", self.__stock)

    def calcular_precio_final(self):
      
        return self.precio

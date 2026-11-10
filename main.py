from producto import Producto
from alimento import Alimento
from electronico import Electronico
from ropa import Ropa

#objetos
leche = Alimento("Leche", 2000, 10, "30/11/2026")
notebook = Electronico("Notebook", 800000, 4, 12)
cuaderno = Producto("Cuaderno", "Librería", 5000, 20)
remera = Ropa("Remera", 12000, 15, "M", "Remera")
pantalon = Ropa("Pantalón", 25000, 8, "42", "Pantalón")

# los objetos se guardan en una sola lista.
productos = [leche, notebook, cuaderno, remera, pantalon]



# EJERCICIO 1

print("\nPRECIOS FINALES ")

for producto in productos:
    precio_final = producto.calcular_precio_final()
    print(producto.nombre, "- Precio final: $", round(precio_final, 2))






# EJERCICIO 2

print("\n DATOS ESPECÍFICOS ")

leche.mostrar_vencimiento()
notebook.mostrar_garantia()
remera.mostrar_talle()
pantalon.mostrar_talle()



# EJERCICIO 3


print("\n PRUEBAS DE STOCK ")

# Venta válida.
print("\nVenta válida de 2 leches:")
print("Stock antes:", leche.get_stock())
leche.vender(2)
print("Stock después:", leche.get_stock())

# Venta con stock insuficiente.
print("\nVenta de 20 notebooks:")
print("Stock antes:", notebook.get_stock())
notebook.vender(20)
print("Stock después:", notebook.get_stock())

# Reposición.
print("\nReposición de 5 notebooks:")
print("Stock antes:", notebook.get_stock())
notebook.reponer(5)
print("Stock después:", notebook.get_stock())




print("\n LISTA COMPLETA DE PRODUCTOS ")

for producto in productos:
    print("\n")
    producto.mostrar_datos()
    print("Precio final por unidad: $", round(producto.calcular_precio_final(), 2))




print("\n VALOR DEL INVENTARIO")

valor_total = 0

producto_mas_caro = productos[0]
mayor_precio = producto_mas_caro.calcular_precio_final()

for producto in productos:
    precio_final = producto.calcular_precio_final()
    valor_producto = producto.get_stock() * precio_final
    valor_total += valor_producto

    print(
        producto.nombre,
        "| Stock:", producto.get_stock(),
        "| Precio final: $", round(precio_final, 2),
        "| Valor del stock: $", round(valor_producto, 2)
    )

    
    if precio_final > mayor_precio:
        mayor_precio = precio_final
        producto_mas_caro = producto

print("\nValor total del inventario: $", round(valor_total, 2))
print(
    "Producto de mayor precio final:",
    producto_mas_caro.nombre,
    "($", round(mayor_precio, 2), ")"
)


# --------------------------------------------------
# PREGUNTAS PARA DEFENDER EL PROGRAMA
# Respuestas incluidas como comentarios para la entrega.
# --------------------------------------------------

# 1) ¿Qué diferencia hay entre heredar un método y sobrescribirlo?
# Heredar es utilizar un método que ya está definido en la clase padre.
# Sobrescribir es crear en la clase hija otro método con el mismo nombre,
# para cambiar o especializar su comportamiento.

# 2) ¿Por qué el mismo for puede invocar calcular_precio_final()
#    en todos los productos sin usar if por tipo?
# Porque todos los objetos tienen ese método. Cada clase ejecuta su propia
# versión, gracias al polimorfismo.

# 3) ¿Qué inicializa super().__init__(...) en cada clase hija?
# Inicializa los atributos comunes definidos en Producto: nombre, tipo,
# precio y stock.

# 4) ¿Qué diferencia hay entre vender(5), reponer(5) y set_stock(5)?
# vender(5) descuenta cinco unidades si hay stock suficiente.
# reponer(5) suma cinco unidades al stock actual.
# set_stock(5) establece el stock directamente en cinco unidades,
# siempre que el valor sea válido.

# 5) Identificá una línea que demuestre encapsulamiento, herencia
#    y polimorfismo.
# Encapsulamiento: self.__stock = 0 (en producto.py).
# Herencia: class Alimento(Producto) (en alimento.py).
# Polimorfismo: producto.calcular_precio_final() dentro del for (en main.py).

# 6) ¿Qué responsabilidad tiene main.py y por qué separamos las clases?
# main.py es el punto de entrada: crea objetos, arma la lista, prueba
# operaciones y muestra resultados. Separamos las clases para organizar
# el proyecto, facilitar su lectura y mantener cada responsabilidad
# en su propio archivo.

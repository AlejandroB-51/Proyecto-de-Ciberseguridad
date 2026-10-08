producto = {
    "nombre" : "Laptop",
    "precio" : 15000,
    "categoría" : "Electrónica",
    "disponible" : True
    }
print("=== Ficha de Producto===")
print(f"Nombre: {producto['nombre']}")
print(f"Precio: ${producto['precio']}")
print(f"Categoría: {producto['categoría']}")
if producto["disponible"] == True:
    print("Disponible: Sí")
else:
    print("Disponible: No")

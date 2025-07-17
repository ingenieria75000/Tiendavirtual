# catalogo.py

productos = {
    "tecnologia": ["Celular Samsung", "Laptop Lenovo", "Audífonos Bluetooth"],
    "ropa": ["Camiseta Polo", "Pantalón Jean", "Chaqueta de cuero"],
    "hogar": ["Sofá de 3 puestos", "Mesa de comedor", "Lámpara LED"]
}

def mostrar_catalogo():
    print("\n=== Catálogo completo ===")
    for categoria, items in productos.items():
        for item in items:
            print(f"- {item} [{categoria}]")

def obtener_categorias():
    return list(productos.keys())

def mostrar_por_categoria(nombre_categoria):
    if nombre_categoria in productos:
        print(f"\nProductos en la categoría '{nombre_categoria}':")
        for item in productos[nombre_categoria]:
            print(f"- {item}")
    else:
        print("❌ Categoría no válida.")

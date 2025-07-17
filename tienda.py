# tienda.py

import catalogo

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Ver catálogo completo")
    print("2. Filtrar por categoría")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2 o 3): ").strip()

        if opcion == "1":
            catalogo.mostrar_catalogo()
        elif opcion == "2":
            categorias = catalogo.obtener_categorias()
            print("\nCategorías disponibles:")
            for cat in categorias:
                print(f"- {cat}")
            seleccion = input("Escribe una categoría exactamente como aparece: ").strip().lower()
            catalogo.mostrar_por_categoria(seleccion)
        elif opcion == "3":
            print("👋 Gracias por visitar la tienda.")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

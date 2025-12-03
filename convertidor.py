def mostrar_menu():
    print("\n" + "="*40)
    print(" 🔄 CONVERTIDOR UNIVERSAL DE UNIDADES")
    print("="*40)
    print("1. Temperatura (Celsius <-> Fahrenheit)")
    print("2. Longitud (Metros <-> Pies)")
    print("3. Peso (Kilogramos <-> Libras)")
    print("4. Almacenamiento (MB <-> GB)")
    print("5. Salir")
    print("="*40)

def convertir_temperatura():
    print("\n--- Temperatura ---")
    try:
        c = float(input("Ingrese grados Celsius: "))
        f = (c * 9/5) + 32
        print(f"✅ Resultado: {c}°C equivalen a {f:.2f}°F")
    except ValueError:
        print("❌ Error: Por favor ingrese un número válido.")

def convertir_longitud():
    print("\n--- Longitud ---")
    try:
        m = float(input("Ingrese metros: "))
        ft = m * 3.28084
        print(f"✅ Resultado: {m} metros equivalen a {ft:.2f} pies")
    except ValueError:
        print("❌ Error: Por favor ingrese un número válido.")

def convertir_peso():
    print("\n--- Peso ---")
    try:
        kg = float(input("Ingrese kilogramos: "))
        lb = kg * 2.20462
        print(f"✅ Resultado: {kg} kg equivalen a {lb:.2f} libras")
    except ValueError:
        print("❌ Error: Por favor ingrese un número válido.")

def convertir_almacenamiento():
    print("\n--- Almacenamiento (Datos) ---")
    print("1. Megabytes a Gigabytes")
    print("2. Gigabytes a Megabytes")
    opcion = input("Seleccione (1/2): ")
    
    try:
        valor = float(input("Ingrese el valor: "))
        if opcion == '1':
            gb = valor / 1024
            print(f"✅ Resultado: {valor} MB son {gb:.4f} GB")
        elif opcion == '2':
            mb = valor * 1024
            print(f"✅ Resultado: {valor} GB son {mb:.2f} MB")
        else:
            print("❌ Opción no válida")
    except ValueError:
        print("❌ Error: Ingrese un número numérico.")

# --- BLOQUE PRINCIPAL (Algoritmo Central) ---
def main():
    while True:
        mostrar_menu()
        opcion = input("👉 Seleccione una opción (1-5): ")

        if opcion == '1':
            convertir_temperatura()
        elif opcion == '2':
            convertir_longitud()
        elif opcion == '3':
            convertir_peso()
        elif opcion == '4':
            convertir_almacenamiento()
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el convertidor! Cerrando sistema...")
            break
        else:
            print("\n❌ Opción desconocida, intente de nuevo.")
        
        input("\nPresione ENTER para continuar...") # Pausa para leer resultado

if __name__ == "__main__":
    main()
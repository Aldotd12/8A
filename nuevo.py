'''Calculadora en python haciendo uso de buenas practicas'''

def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b

def restar(a: float, b: float) -> float:
    """Devuelve la resta de dos números."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Devuelve la multiplicación de dos números."""
    return a * b

def dividir(a: float, b: float) -> float:
    """Devuelve la división de dos números. Lanza una excepción si el divisor es cero."""
    if b == 0:
        raise ValueError("Error: División por cero no permitida")
    return a / b

def mostrar_menu() -> None:
    """Muestra el menú de opciones disponibles en la calculadora."""
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numero(mensaje: str) -> float:
    """Solicita al usuario un número y lo convierte a float."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número válido.")

def calculadora() -> None:
    """Función principal que ejecuta la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Adiós!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = obtener_numero("Introduce el primer número: ")
            num2 = obtener_numero("Introduce el segundo número: ")

            try:
                if opcion == '1':
                    print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecutar la calculadora si el script se ejecuta directamente
if __name__ == "__main__":
    calculadora()

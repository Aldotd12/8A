'''Este archivo realiza una sumatoria y otras operaciones básicas'''
VALOR_UNO = 2
VALOR_DOS = 5
RESULTADO_FINAL = VALOR_UNO + VALOR_DOS
print(RESULTADO_FINAL)

if RESULTADO_FINAL % 2 == 0:
    print(f"El resultado {RESULTADO_FINAL} es par")
else:
    print(f"El resultado {RESULTADO_FINAL} es impar")

def suma(num1, num2):
    """Devuelve la suma de dos números."""
    return num1 + num2

def resta(num1, num2):
    """Devuelve la resta de dos números."""
    return num1 - num2

def multiplicacion(num1, num2):
    '''Devuelve la multiplicación de dos números.'''
    return num1 * num2

def division(num1, num2):
    '''Devuelve la división de dos números. Lanza una excepción si el divisor es cero.'''
    return num1 / num2

print(f"Suma: {suma(VALOR_UNO, VALOR_DOS)}")
print(f"Resta: {resta(VALOR_UNO, VALOR_DOS)}")
print(f"Multiplicación: {multiplicacion(VALOR_UNO, VALOR_DOS)}")
print(f"División: {division(VALOR_UNO, VALOR_DOS)}")

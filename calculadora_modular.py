def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "no se puede dividir entre cero."
    return a / b
def obtener_numeros():
    try:
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        return num1, num2
    except ValueError:
        print("debe ingresar valores numericos.")
        return None, None
def mostrar_menu():
    print("\n calculadora modular ")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
while True:
    mostrar_menu()
    opcion = input("seleccione una opcion: ")
    if opcion == "5":
        print("saliendo de la calculadora...")
        break
    if opcion in ["1", "2", "3", "4"]:
        num1, num2 = obtener_numeros()
        if num1 is None:
            continue
        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)
        print(f"resultado: {resultado}")
    else:
        print("opcion invalida.")
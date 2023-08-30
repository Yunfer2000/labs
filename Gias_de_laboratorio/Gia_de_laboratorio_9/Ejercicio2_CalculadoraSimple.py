def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("No se puede dividir entre cero.")
    return x / y

def main():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operation = input("Selecciona la operación (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Operación no válida. Debe ser +, -, *, o /.")
            return

        print(f"Resultado: {result}")

    except ValueError:
        print("Entrada inválida. Debes ingresar números válidos.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
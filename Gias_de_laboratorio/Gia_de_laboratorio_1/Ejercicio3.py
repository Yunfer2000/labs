def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial(numero - 1)

def main():
    numero = int(input("Ingresa un número: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")

if __name__ == "__main__":
    main()
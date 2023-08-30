def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperature = float(input("Ingresa la temperatura: "))
        unit = input("Ingresa la unidad de temperatura (C o F): ").upper()

        if unit == 'C':
            converted_temperature = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C equivale a {converted_temperature:.2f}°F")
        elif unit == 'F':
            converted_temperature = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F equivale a {converted_temperature:.2f}°C")
        else:
            print("Unidad no válida. Debe ser 'C' o 'F'.")

    except ValueError:
        print("Entrada inválida. Debe ingresar un número válido.")

if __name__ == "__main__":
    main()
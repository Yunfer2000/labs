def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    numero = int(input("Ingresa un número: "))
    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")

if __name__ == "__main__":
    main()
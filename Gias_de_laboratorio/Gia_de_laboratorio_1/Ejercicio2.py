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

def numeros_primos_menores_que_n(n):
    primos = []
    for num in range(2, n):
        if es_primo(num):
            primos.append(num)
    return primos

def main():
    n = int(input("Ingresa un número n: "))
    primos = numeros_primos_menores_que_n(n)
    print(f"Números primos menores que {n}: {primos}")

if __name__ == "__main__":
    main()
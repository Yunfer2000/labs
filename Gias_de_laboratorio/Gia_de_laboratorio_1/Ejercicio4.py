def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    n = int(input("Ingresa el n-ésimo término: "))
    serie_fibonacci = fibonacci(n)
    print(f"Serie de Fibonacci hasta el {n}-ésimo término:", serie_fibonacci)

if __name__ == "__main__":
    main()
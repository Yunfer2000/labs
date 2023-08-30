def main():
    print("N  N^1 N^2 N^3 N^4")
    print("-" * 21)
    
    for n in range(1, 6):
        n_1 = n
        n_2 = n ** 2
        n_3 = n ** 3
        n_4 = n ** 4
        print(f"{n}  {n_1}   {n_2}   {n_3}   {n_4}")

if __name__ == "__main__":
    main()
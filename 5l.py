N = int(input("Enter N: "))
result = 0
factorial = 1

if not (N <= 0):
    for i in range(1, N+1):
        for j in range(1, i+1):
            factorial *= j
        result += factorial
        factorial = 1

    print(f"The sum of factorials is {result}")
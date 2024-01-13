A = float(input("Enter number A: "))
N = int(input("Enter number N: "))
result = 0

if not (N <= 0):
    for i in range(1, N+1):
        print(A**i)
else:
    print("Invalid input")
N = int(input("Enter a number: "))
sum = 0

for i in range(N+1):
    sum += (N + i)**2

print(f"The sum of the expression is equal to {sum}")
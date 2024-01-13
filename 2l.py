A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
product = 1

if A < B:
    for i in range(A, B+1):
        product *= i
    print(f'Product of all numbers between {A} and {B} equals {product}')
elif A >= B:
    print("Not valid values")
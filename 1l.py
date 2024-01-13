A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
sum = 0

if A < B:
    for i in range(A, B+1):
        sum += i
    print(f'Sum of all numbers between {A} and {B} equals {sum}')
elif A >= B:
    print("Not valid values")
#1c
"""number = int(input("Whole number "))
if number > 0:
    number += 1
elif number < 0:
    number -= 2
elif number == 0:
    number = 10
print(f"The resulting number is {number}")"""
#2c
"""a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
positive = 0
negative = 0
numbers = [a, b, c]
for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print(f"The amount of positive numbers is: {positive}")
print(f"The amount of negative numbers is: {negative}")"""
#3c
"""a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
result = 0
if a >= b and a >= c:
    result = a + max(b, c)
elif b >= a and b >= c:
    result = b + max(a, c)
else:
    result = c + max(a, b)
print(f"The sum of the two largest numbers is {result}")"""
#4c
"""number = int(input('Enter a number: '))
if number % 2 == 0:
    print('Even')
else:
    print('Odd')"""
#5c
"""xaxis = float(input('Enter x-axis number: '))
yaxis = float(input('Enter y-axis number: '))
if xaxis > 0 and yaxis > 0:
    print('Point lies in I quadrant')
elif xaxis < 0 and yaxis > 0:
    print('Point lies in II quadrant')
elif xaxis < 0 and yaxis < 0:
    print('Point lies in III quadrant')
elif xaxis > 0 and yaxis < 0:
    print('Point lies in IV quadrant')"""
#1l
"""A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
sum = 0

if A < B:
    for i in range(A, B+1):
        sum += i
    print(f'Sum of all numbers between {A} and {B} equals {sum}')
elif A >= B:
    print("Not valid values")"""
#2l
"""A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
product = 1

if A < B:
    for i in range(A, B+1):
        product *= i
    print(f'Product of all numbers between {A} and {B} equals {product}')
elif A >= B:
    print("Not valid values")"""
#3l
"""N = int(input("Enter a number: "))
sum = 0

for i in range(N+1):
    sum += (N + i)**2

print(f"The sum of the expression is equal to {sum}")"""
#4l
"""A = float(input("Enter number A: "))
N = int(input("Enter number N: "))
result = 0

if not (N <= 0):
    for i in range(1, N+1):
        print(A**i)
else:
    print("Invalid input")"""
#5l
"""N = int(input("Enter N: "))
result = 0
factorial = 1

if not (N <= 0):
    for i in range(1, N+1):
        for j in range(1, i+1):
            factorial *= j
        result += factorial
        factorial = 1

    print(f"The sum of factorials is {result}")"""
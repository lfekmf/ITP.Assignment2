a = int(input('Enter first number: '))
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
print(f"The amount of negative numbers is: {negative}")
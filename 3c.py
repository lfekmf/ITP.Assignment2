a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
result = 0
if a >= b and a >= c:
    result = a + max(b, c)
elif b >= a and b >= c:
    result = b + max(a, c)
else:
    result = c + max(a, b)
print(f"The sum of the two largest numbers is {result}")
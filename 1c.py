number = int(input("Whole number "))
if number > 0:
    number += 1
elif number < 0:
    number -= 2
elif number == 0:
    number = 10
print(f"The resulting number is {number}")
sum_positive = 0
while True:
    number = int(input("Enter a number (negative number to exit): "))
    if number >= 0:
        sum_positive += number
    else:
        break
print("Sum of positive numbers:", sum_positive)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
maximum = max(num1, num2)
while True:
    if maximum % num1 == 0 and maximum % num2 == 0:
        lcm = maximum
        break
    maximum += 1
print("(LCM) of", num1, "and", num2, "is:", lcm)



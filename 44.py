base = int(input("Enter the base number: "))
expo = int(input("Enter the exponent: "))

result = 1

for i in range(1, expo + 1):
    result *= base

print("The result of", base, "raised to the power of", expo, "is:", result)


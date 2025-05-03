num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % num2 == 0:
    result = "divisible"
else:
    result = "not divisible"
print(f"The first number is {result} by the second number.")
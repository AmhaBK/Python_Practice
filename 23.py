num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: ")) 
sumn = num1 + num2 + num3 
if sumn % 5 == 0:
    print("The sum is divisible by 5.")
else:
    print("The sum is not divisible by 5.")
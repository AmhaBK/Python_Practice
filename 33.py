num = int(input("Enter an integer: ")) 
if num % 3 == 0 and num % 5 == 0:
    result = "divisible by 3 and 5"
else:
    result = "not divisible by 3 and 5"
print(f"The number {num} is {result}.")
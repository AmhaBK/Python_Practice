number = int(input("Enter a number: "))

previous_number = 0
current_number = 1

print("Fibonacci sequence up to", number, ":")
print(previous_number, end=" ")

while current_number <= number:
    print(current_number, end=" ")

    next_number = previous_number + current_number

    previous_number = current_number
    current_number = next_number


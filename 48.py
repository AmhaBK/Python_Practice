N = int(input("Enter the value of N: "))

count = 0
num = 1

while count < N:
    square = num ** 2

    print(square, end=" ")
    count += 1

    num += 1

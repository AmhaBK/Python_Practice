a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

start = min(a, b)
end = max(a, b)

for num in range(start, end + 1):
    print(num, end=" ")

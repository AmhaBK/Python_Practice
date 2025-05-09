n = int(input("Enter the size of the array: "))

array = []

print("Enter elements for the array:")
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    array.append(element)

target = int(input("Enter the number to search for: "))

count = 0
for element in array:
    if element == target:
        count += 1

print("The number", target, "appears", count, "time(s) in the array.")


n = int(input("Enter the number of elements: "))
array = []

for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    array.append(element)

largest = array[0]

for i in range(1, n):
    if array[i] > largest:
        largest = array[i]

print("Largest element:", largest)


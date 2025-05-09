size = int(input("Enter the size of the arrays: "))

array1 = []
array2 = []

print("Enter elements for array 1:")
for i in range(size):
    element = int(input("Enter element {}: ".format(i + 1)))
    array1.append(element)

print("Enter elements for array 2:")
for i in range(size):
    element = int(input("Enter element {}: ".format(i + 1)))
    array2.append(element)

result_array = []

for i in range(size):
    result = array1[i] * array2[i]
    result_array.append(result)

print("Resulting array:", result_array)



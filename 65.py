n = int(input("Enter the size of the array: "))
array = []
print("Enter elements for the array:")
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    array.append(element)

is_ascending = True

for i in range(1, n):
    if array[i] < array[i - 1]:
        is_ascending = False
        break

if is_ascending:
    print("The array is in ascending order.")
else:
    print("The array is not in ascending order.")


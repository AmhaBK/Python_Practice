size = int(input("Enter the size of the array: "))

array = []

print("Enter elements for the array:")
for i in range(size):
    element = int(input("Enter element {}: ".format(i + 1)))
    array.append(element)

all_even = True

for element in array:
    if element % 2 != 0:
        all_even = False
        break

if all_even:
    print("All elements are even.")
else:
    print("Not all elements are even.")



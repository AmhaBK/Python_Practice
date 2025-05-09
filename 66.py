n = int(input("Enter the size of the array: "))

array = []

print("Enter elements for the array:")
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    array.append(element)

start = 0
end = n - 1
while start < end:
    array[start], array[end] = array[end], array[start]
    start += 1
    end -= 1

print("Elements in reverse order:")
for element in array:
    print(element)


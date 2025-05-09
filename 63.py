n = int(input("Enter the number of elements: "))

array = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    array.append(element)
sum = 0
for element in array:
    sum += element

average = sum / n

print("Average:", average)


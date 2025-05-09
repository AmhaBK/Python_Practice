n = int(input("Enter the size of the vectors: "))
vector1 = []
vector2 = []
print("Enter elements for vector 1:")
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    vector1.append(element)
print("Enter elements for vector 2:")
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    vector2.append(element)

result_vector = []
for i in range(n):
    sum_element = vector1[i] + vector2[i]
    result_vector.append(sum_element)
print("Resulting vector (sum of corresponding elements):", result_vector)


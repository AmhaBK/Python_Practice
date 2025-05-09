import math
x = float(input("Enter the value of x: "))
sum = 1
term = 1
for n in range(1, 11):
    term *= x / n
    sum += term

result = math.exp(x)
print("Approximation of e^x:", sum)
print("Actual value of e^x:", result)


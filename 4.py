import math
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: ")) 
mult = num1 * num2 * num3 
geoMean = math.pow(mult, 1/3)
print("Geometric mean is: ", geoMean)
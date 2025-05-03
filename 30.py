grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float (input("Enter the third grade: "))
average_grade = (grade1 + grade2 + grade3) / 3 
if average_grade >= 7:
    result = "Pass"
elif average_grade < 4:
    result = "Fail"
else:
    result = "Recovery" 
print("The student's final result is:", result)
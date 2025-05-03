grade1 = float(input("Enter the grade of the first test: ")) 
grade2 = float(input("Enter the grade of the second test: ")) 
average = (grade1 + grade2) / 2 
if average >= 6:
    print("The student passed with an average of", average) 
else:
    print("The student failed with an average of", average)
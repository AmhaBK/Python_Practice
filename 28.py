import datetime
year_of_birth = int(input("Enter the year of birth: "))
current_year = datetime.datetime.now().year 
age = current_year - year_of_birth 
if age >= 16:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")
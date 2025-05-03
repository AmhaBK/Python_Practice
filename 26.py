age1= int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: ")) 
legal_age_count = 0
if age1 >= 18:
    legal_age_count + 1
if age2 >= 18:
    legal_age_count += 1
if age3 >= 18:
    legal_age_count += 1
print("Out of the three people,", legal_age_count, "person(s) is/are of legal age.")
age = int(input("Enter your age: ")) 
if age <= 12:
    category = "Child"
elif age <= 17:
    category = "Teenager"
elif age <= 59:
    category = "Adult"
else:
    category = "Elderly" 
print("You are a", category + ".")
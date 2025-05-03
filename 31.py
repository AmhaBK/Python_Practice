day = input("Enter the name of a day: ") 
day = day.lower() 
if day == "saturday" or day == "sunday":
    result = "Weekend day"
else:
    result = "Weekday" 
print(f"{day.capitalize()} is a {result}.")
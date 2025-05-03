age = int(input("Enter your age: ")) 
if age < 16:
    print("You are not able to vote.")
elif age >= 18 and age <= 69:
    print("yoting is obligatory for you.")
else:
    print("You are able to vote, but it is not obligatory.")
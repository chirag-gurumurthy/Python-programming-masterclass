name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age <= 30:
    print("Welcome to club 18-30 holidays, {}".format(name))
else:
    print("You are not in the age group to enter this club")

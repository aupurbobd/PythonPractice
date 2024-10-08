height = int(input("Enter your height:"))
if height > 3:
    print("You are eligible for the ride.")
    age=int(input("Enter your age:"))
    if age<=12:
        print("Please pay 2 euro.")
    elif age<=18:
        print("Please pay 3 euros.")
    else:
        print("Please pay 5 Euro.")
    print("Please have a nice ride.")
else:
    print("You're not eligible for the ride.")
print("bye")
height = int(input("Enter your height:"))
if height > 3:
    print("You are eligible for the ride.")
    age=int(input("Enter your age:"))
    if age<=12:
        bill = 2
        print(f"Ticket price: {bill} euros.")
    elif age<=18:
        bill=3
        print(f"Ticket price: {bill} euros.")
    else:
        bill=5
        print(f"Ticket price: {bill} euros.")
    want_photo=input("Taking photos charges extra 1 euro. Do you want to take photos? (Y/N):")
    if want_photo=='Y' or want_photo == 'y':
        bill=bill+1
    print(f"Please pay {bill} euros. Have a nice ride.")
else:
    print("You're not eligible for the ride.")
print("bye")
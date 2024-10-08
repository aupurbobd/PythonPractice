print("(S)mall Pizza 6 euros || (M)edium Pizza 8 euros || (L)arge Pizza 10 euros")
pflag=0
price=0
pizza_size=input("Which size of pizza do you want? (S/M/L):")
if pizza_size == 's' or pizza_size=='S':
    price=6
    pflag=1
    print(f"Pizza price: {price}.")
    print("Pepperoni costs extra 2 euros.")
    pep=input("You want Pepperoni? (Y/N): ")
    if pep=="y" or pep == "YY":
        price=2+price
elif pizza_size == 'm' or pizza_size == 'M':
    price = 8
    pflag=1
    print(f"Pizza price: {price}.")
    print("Pepperoni costs extra 3 euros.")
    pep = input("You want Pepperoni? (Y/N): ")
    if pep == "y" or pep == "YY":
        price = 3+price

elif pizza_size == 'l' or pizza_size == 'L':
    price = 10
    pflag=1
    print(f"Pizza price: {price}.")
    print("Pepperoni costs extra 3 euros.")
    pep = input("You want Pepperoni? (Y/N): ")
    if pep == "y" or pep == "YY":
        price = 3+price
else:
    print("Invalid pizza selection! please try again.")
if pflag==1:
    cheese=input("Extra cheese price: 1 euro. want some? (Y/N):")
    if cheese =='y' or cheese == 'Y':
        price=price + 1
    print(f"Total bill is {price}")

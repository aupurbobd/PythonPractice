import random
names=input("Enter the name of the team members:")
name_list=names.split(" ")
print(name_list)
winner=random.choice(name_list)
print(f"The winner is: {winner}")

w=random.randint(0, len(name_list)-1)
winner2=name_list[w]
print(f"The second winner is: {winner2}")

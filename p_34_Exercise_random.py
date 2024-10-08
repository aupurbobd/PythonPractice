import random

options=[0,1]
c=random.choice(options)
print(c)

if c==1:
    print("Head")
else:
    print("Tail")

t=random.randint(0,1)

if t==1:
    print("Head")
else:
    print("Tail")
import random
print(random.randint(1,50))

l=[4, 5, 2, 8, 6]
c=random.choices(l)
print(c)
random.shuffle(l)
print(l)
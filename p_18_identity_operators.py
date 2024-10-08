a,b=4,4
c="4"
print(id(a))
print(id(b))
print(a is b)
print(id(c))
d=int(c)
print(id(d))
print(c is d)
print(a is d)
print(c is not d)
print(a is not d)
a=input("Enter the value of a =")
b=input("Enter the value of b =")

print("a = ",a)
print("b = ",b)
print(a+b)

c=a
a=b
b=c
print("After swapping the numbers:")
print("a = ",a)
print("b = ",b)

a=int(a)
b=int(b)
a=a+b
b=a-b
a=a-b
print("After swapping the numbers again:")
print("a = ",a)
print("b = ",b)
import random
c=1
while c<=5:
    print(c)
    c+=1
else:
    print('While loop is over')

list1=[1,2,3,4,5,6,7,8,9,10]
count=0
while list1:
    r=random.choice(list1)
    print(r)
    list1.pop()
    count+=1
    if r==4:
        break
else:
    print(f'Loop traversed {count} times')

count=1
while count<1:
    print('This loop will not run')
total=0
while True:
    n=int(input('Enter a number to add (0 to quit):'))
    if n==0:
        break
    else:
        total+=n
else:
    print("this will never be printed")
print(f"The total is {total}")


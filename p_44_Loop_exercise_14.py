height_input=input("Enter a list of heights seperated by space:")
list1=height_input.split(" ")
print(list1)
s=0
c=0
for i in list1:
    s+=int(i)
    c+=1
print(f'Sum={s}')
print(f'count ={c}')
avarage=s/c
print(f'The average height is {avarage}')
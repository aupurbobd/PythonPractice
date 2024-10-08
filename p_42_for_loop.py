t=(2, 3, 4, 5,3)
for i in t:
    print(i)
set1={'Jahangir', 'Neela', 'Sheuli', 'Shila'}
set2={'Jahangir', 'Neela',"Wasee", "Zahraa"}
for name in set1:
    print(name)

list1=[4, 1, -2, 5, 100]
c=0
for i in list1:
    c+=i
print(c)
list2=[5, 9, 3, 0, 6, 8]
list3=[]
l=len(list2)
for i in range(0,l-1):
    list3.append(list2[i]**2)
    if list2[i]==0:
        print('list not fully traversed')
        break
else:
    print(f'list is completed')
print(list3)
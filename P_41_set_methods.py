set1={'Jahangir', 'Neela', 'Sheuli', 'Shila'}
set2={'Jahangir', 'Neela',"Wasee", "Zahraa"}

set3=set1.union(set2)
set4=set2.union(set1)

print(set1)
print(set2)
print(set3)
print(set4)
set5=set1.intersection(set2)
print(set5)
print(f'set1 = {set1}')
set6=set1.intersection_update(set2)
print(f'set1 = {set1}')
print(set6)
set7=set1.symmetric_difference(set2)
print(set7)
set8=set1.union(set7)
print(set1)
print(set8)

list1=[1,5,3]
set9=set1.update((list1))
print(set9)
print(set1)
set1={'Jahangir', 'Neela', 'Sheuli', 'Shila'}
set2={'Jahangir', 'Neela',"Wasee", "Zahraa"}

set3=set1.difference(set2)
print(set1)
print(set3)
print(set2-set1)

#set1.difference_update(set2)
print(set1)
print(set2)
set4=set1.symmetric_difference(set2)
set5=set1.union(set2)
set6=set1.intersection(set2)
set7=set5-set6
print(set5)
print(set6)
print(set4)
print(set7)
set8=set1 ^ set2
print(set8)
set9=set1 ^ set2 ^ set8
print(set9)
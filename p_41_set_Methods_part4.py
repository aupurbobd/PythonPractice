set1={'Jahangir', 'Neela', 'Sheuli', 'Shila'}
set2={'Jahangir', 'Neela',"Wasee", "Zahraa"}
set3={4,2,7,5}
set4={"Jahangir","Neela"}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
disjoin =set1.isdisjoint(set2)
print(disjoin)
print(set1.issubset(set2))
print(set4.issubset(set1))
print(set1.issuperset(set4))
family = ['Wasee', "Zahraa", "Jahangir", 'Neela', 2, 4, 9]
print(family)
print(len(family))
print(family[-1])
print(family[2:3])
print(family[1:7:3])
#family.sort()
family.append(3 )
print(family)
family.insert(4,0)
print(family)
##family.extend("new member")
#print(family)
family[6:9]=133,142,125
print(family)
family.remove(125)
print(family)
popped_value=family.pop()
print(family)
print(popped_value)
popped_value=family.pop(5)
print(family)
print(popped_value)

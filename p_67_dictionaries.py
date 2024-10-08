student_info={
    1:'Mithun',
    2:'Baker',
    3:'Harun',
    1:'Rafiq'
}
print(student_info[1])

phone_no=dict({'Jahangir':'041234','Neela':54339})
print(phone_no)

phone_no['Jahangir']=417257002
print(phone_no)

phone_no['Wasee']={234567, 56432, 5678}
print(phone_no)

phone_no['Neela'] = {'Home':87654, 'work':'0175933'}
print(phone_no)
print(phone_no['Neela'])
print(phone_no['Neela']['Home'])

del phone_no['Jahangir']
print(phone_no)
print(phone_no.keys())
print(phone_no.items())
print(phone_no.values())
phone_no['Zahraa']=987653
print(phone_no.items())
for i in phone_no:
    print(i)
    print(phone_no[i])

for i in phone_no.items():
    print(i)
phone_no={'Jahangir':{'home':'01749334873','Finnish':'0417257002'},'Neela':('04175773045','0417254089'), 'Nipa':'0406581203'}
print(phone_no.keys())
print(phone_no.values())
print(phone_no)
print(phone_no.items())
print(phone_no['Jahangir']['home'])
print(phone_no['Neela'])
print(phone_no['Neela'][0])
phone_no['Jahangir']['office']='0191583249'
print(phone_no['Jahangir'])
print(phone_no['Jahangir'].pop('office'))
print(phone_no['Jahangir'])

phone_book=[{'Jahangir':{'home':'01749334873','Finnish':'0417257002'}},{'Neela':('04175773045','0417254089')}]
print(phone_book[1])
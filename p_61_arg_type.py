#types of Arguments
#default
#positional
#arbitrary/variable length
          #Arbitrary positional
          #Arbitrary keyword
def introduction(name, age=6, city='Dhaka'):
    print(f'Hello! I am {name}.')
    print(f'I am {age} years of old.')
    print(f'I live in {city}.')

introduction('Jahangir',45, 'Lappeenranta')
introduction(age=35, city='Lappeenranta', name="Neela")
introduction("Wasee",city='Lappeenranta', age=9)
introduction('Moktarul',35)
introduction(name='Zahraa',city='Lappeenranta')
introduction('Raina')
#Arbitrary arguments
def add(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
print(add(5,6,7,8,9,))
print(add(5,1,7))


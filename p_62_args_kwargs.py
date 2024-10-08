# *args

#Arbitrary arguments
def add(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
print(add(5,6,7,8,9,))
print(add(5,1,7))
print(f'The summation is {add(7,15,24,25,17,277)}')

def calc(*numbers, operator):
    result=0
    if operator=='+':
        for i in numbers:
            result+=i
    elif operator=='*':
        result=1
        for i in numbers:
            result*=i
    return result

print(calc(3, 5, 6, 7, operator='*'))
print(calc(4, 8, 2, 5, operator='+'))

def calculate(op, *numbers):
    result = 0
    if op == '+':
        for i in numbers:
            result += i
    elif op == '*':
        result = 1
        for i in numbers:
            result *= i
    return result

print(calculate('+',4,5,6,7))
print(calculate('*',4,5,6,7,8,9))

#KeyWordArgument

def personalinfo(**info):
    for key, value in info.items():
        print(f'{key} ={value}')
personalinfo(name='Jahangir', address='Karankokatu')
personalinfo(name='Neela', age=35)

def info(*args, **kwargs):
    for key, value in kwargs.items():
        print(f'{key} ={value}')
    sum=0
    for i in args:
        sum=sum+i
    print(f'Summation is {sum}')

info(1, 2,3, Name='Jahangir', roll=5)

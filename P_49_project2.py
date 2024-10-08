import random
letters = ['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

letter_count=int(input('How many letters do you want to include:'))
number_count=int(input("How many numbers to include in the password:"))
symbol_count =int(input('How many symbols to be included:'))

password_list=[]
for i in range(0,letter_count):
    lp=random.choice(letters)
    password_list+=lp
print(password_list)

for i in range(0,number_count):
    np=random.choice(numbers)
    password_list+=np
print(password_list)

for i in range(0,symbol_count):
    sp=random.choice(symbols)
    password_list+=sp
print(password_list)
random.shuffle(password_list)
print(password_list)

password=''

for i in password_list:
    password+=i

print(f'Your password is {password}')
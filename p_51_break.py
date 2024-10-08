import random
numbers=[1,2,3,4,5,6,7,8,9]
print('for loop')
sum=0
for i in numbers:
    sum+=i
    print(f'Number:{i} and sum:{sum}')
    if sum>10:
        break
    random.shuffle(numbers)

#print(sum)
print('While loop')
sum=0
while numbers:
    random.shuffle(numbers)
    midnum=numbers[round(len(numbers)/2)]
    sum=sum+midnum
    print(f'Number:{midnum} and sum:{sum}')
    if sum>10:
        break
import random

targetnumber=random.randint(1,50)
print(targetnumber)
failure=0
while failure<5:
    guess=int(input('Guess a number between 1 and 50:'))
    distance=targetnumber-guess
    if distance==0:
        print('Correct  number! You Won!!')
        break
    else:
        failure+=1
        if distance>10:
            print('Your guess is too low.guess again!!')
        elif distance<-10:
            print('Your guess is too high. guess again!!')
        elif distance<=10 or distance>=-10:
            print('You are almost there! guess again!!')
        print(f'You have {5-failure} attempts left.')
        if failure==5:
            print('Goodbye! Better luck next time.')
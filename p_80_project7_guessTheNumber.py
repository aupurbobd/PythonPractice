import random
import logo
EASY_LEVEL=10
HARD_LEVEL=5

def set_difficulty_level(level):
    if level=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def check_number(target, guessed):
    distance=target-guessed
    if distance==0:
        print('Correct  number! You Won!!')
        return True
    else:
        if distance>10:
            print('Your guess is too low.Try again!!')
        elif distance < -10:
            print('Your guess is too high. Try again!!')
        elif distance <= 10 or distance >= -10:
            print('You are almost there! guess again!!')
        return False



print('***** WELCOME TO "GUESS THE NUMBER" GAME *****')
print(logo.logo)
level_flag=False
diff_level=''
while level_flag==False:
    diff_level=input('Choose the difficulty level (type \'easy\'):')
    if diff_level.lower() not in ('easy','hard'):
        print('Wrong choice! Try again.')
    else:
        level_flag=True
targetnumber=random.randint(1,50)
print(targetnumber)

allowed_attempts=set_difficulty_level(diff_level)
print(f'You have {allowed_attempts} attempts to guess the correct number.')
failure=0
while failure<allowed_attempts:
    guess=int(input('Guess a number between 1 and 50:'))
    check_flag=check_number(targetnumber,guess)
    if check_flag:
        break
    else:
        failure+=1
        if failure<allowed_attempts:
            print(f'You have {allowed_attempts - failure} attempts left.')
        elif failure==allowed_attempts:
            print('You lost! Better luck next time.')

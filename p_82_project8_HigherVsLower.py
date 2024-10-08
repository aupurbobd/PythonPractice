import logo
import random
import profiledatabase
import os


def profile_compare(profile1, profile2, option):
    max=1
    if profile1['follower_count'] > profile2['follower_count']:
        max = 1
        followers = profile1['follower_count']
    else:
        max = 2
        followers = profile2['follower_count']
    if max==option:
        print(logo.correct)
        return True
    else:
        print(logo.loser)
        return False


is_continue=True
while is_continue:

    print(logo.higher)
    profiles=profiledatabase.Data[:]
    option1=random.choice(profiles)
    iscorrect=True
    score=0
    while iscorrect:
        profiles = profiledatabase.Data[:]
        profiles.remove(option1)
        option2 = random.choice(profiles)
        #print(logo.higher)
        print(f'Option 1: {option1["name"]}, {option1["description"]}, from {option1["country"]}')

        print(logo.vs)
        print(f'Option 2: {option2["name"]}, {option2["description"]}, from {option2["country"]}')
        response=int(input('Who has more followers? type 1 or 2:'))
        result=profile_compare(option1,option2, response)

        if result==True:
            score+=1
            print(f'You are right. Your score is {score}')
            option1=option2
        else:
            print(f'Game Over! Your final score is {score}')
            iscorrect=False
    playagain=input("Do you want to play again (Yes or No):")
    if playagain.lower()=='yes':
        os.system('cls')
    else:
        print(logo.goodbye)
        is_continue=False







import logo
import profiledatabase
import random

def displayprofile(profile):
    name = profile['name']
    description = profile['description']
    country = profile['country']
    return f'{name}, {description} from {country}'
def checkresponse(account1, account2, response):
    if account1['follower_count']>account2['follower_count']:
        if response==1:
            return True
        else:
            return False
    else:
        if response==2:
            return True
        else:
            return False

iscontinue=True

while iscontinue:
    print(logo.higher)
    iscorrect=True
    score = 0
    profile1 = random.choice(profiledatabase.Data)
    while iscorrect:



        profile2=random.choice(profiledatabase.Data)
        while profile1==profile2:
            profile2=random.choice(profiledatabase.Data)

        print(f'Profile-1: {displayprofile(profile1)}')
        print(logo.vs)
        print(f'Profile-2: {displayprofile(profile2)}')


        option=int(input('Who has more followers? (type 1 or 2):'))
        result=checkresponse(profile1, profile2, option)
        print(result)
        if result==True:
            score+=1
            print(logo.correct)
            print(f'Your score is {score}')
            profile1=profile2
        else:
            print(logo.loser)
            print(f'Your final score is {score}')
            iscorrect=False
    playagain=input('Do you want to play again? (Type yes or no):')
    if playagain.lower()=='no':
        iscontinue=False
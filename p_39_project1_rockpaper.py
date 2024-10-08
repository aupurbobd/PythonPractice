import random
print('0 - rock || 1 - paper || 2 - Scissor')
uc = int(input("Enter user choice:"))
options=[0,1,2]
cc=random.choice(options)
if uc==0:
    print(f'Your choice:{uc} - rock')
elif uc == 1:
    print(f'Your choice:{uc} - paper')
else:
    print(f'Your choice:{uc} - scissor')

if cc==0:
    print(f'Computer\'s choice:{cc} - rock')
elif cc == 1:
    print(f'Computer\'s choice:{cc} - paper')
else:
    print(f'Computer\'s choice:{cc} - scissor')

if uc==cc:
    print("Result: Draw")
elif uc ==0 and cc==1:
    print("Computer wins")
elif uc==0 and cc==2:
    print('You win')
elif uc==1 and cc==0:
    print('You win')
elif uc== 1 and cc==2:
    print('Computer Wins')
elif uc ==2 and cc==0:
    print("Computer Wins")
elif uc==2 and cc ==1:
    print("You win")
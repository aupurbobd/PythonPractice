import random
print('0 - rock || 1 - paper || 2 - Scissor')
uc = int(input("Enter user choice:"))
if uc <0 or uc>2:
    print("Invalid Choice")
else:
        rock='👊🏾'
        paper='🖐️'
        scissors='🖖'
        images=[rock,paper,scissors]
        options=[0,1,2]
        cc=random.choice(options)
        if uc==0:
            print(f'Your choice:{uc} - rock {images[uc]}')
        elif uc == 1:
            print(f'Your choice:{uc} - paper {images[uc]}')
        else:
            print(f'Your choice:{uc} - scissor {images[uc]}')
        #print(images[uc])
        if cc==0:
            print(f'Computer\'s choice:{cc} - rock {images[cc]}')
        elif cc == 1:
            print(f'Computer\'s choice:{cc} - paper {images[cc]}')
        else:
            print(f'Computer\'s choice:{cc} - scissor {images[cc]}')
        #print(images[cc])

        if uc==cc:
            print("Result: Draw")
        elif uc==0 and cc==2 :
            print('You Won!!')
        elif uc== 2 and cc==0:
            print('Computer Won!!')
        elif uc > cc:
            print("You Won!!")
        elif cc > uc:
            print('Computer Won!!')


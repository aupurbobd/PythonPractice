import random
import p_55_wordfile

#word_list=['cat','mouse','apple','python','fish','orange']
word=random.choice(p_55_wordfile.word_list)
length=len(word)
letters=[]
for i in range(0,length):
    letters.append(word[i])
    #print(word[i])
#print(word[length-1])
#letters=word.split()
#print(word)
#print(letters)
dummys=[]
for i in letters:
    dummys.append('_')
#print(dummys)

f=0
s=0

while f<6 and s==0:
    print(f'The word is {dummys} ')
    guess=input("Choose a letter:")
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                dummys[i]=guess
    else:
        print("wrong choice!")
        f+=1
    if '_' not in dummys:
        s=1
        print(f"You win - the word is {word}")
if f==6:
    print(f"You lost! - the word is {word}")




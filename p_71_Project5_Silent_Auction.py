import os
import random


def winner(bidders):
    maxbid=0
    winner_bidder=''
    for bidder in bidders:
        if maxbid<bidders[bidder]:
            maxbid=bidders[bidder]
            winner_bidder=bidder
    print(f'The winner is {winner_bidder} with price {maxbid}')


bidders=[]
new_bidder={}
flag=True
while flag==True:

    name=input('What is your name?:')
    bid=int(input('What is your bid?:'))
    new_bidder[name]=bid
    #bidders.append(new_bidder)
    more_entry=''
    while more_entry.lower()!='yes' and more_entry.lower()!='no':
        more_entry=input('Are there any other bidder? (yes/no):')
        if more_entry.lower()=='no':
            flag=False
        elif more_entry.lower()=='yes':
            flag=True
        else:
           print('Wrong input! Try again.')
    os.system('cls')
    os.system('cls')
os.system('cls')
winner(new_bidder)





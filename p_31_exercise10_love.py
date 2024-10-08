Yname=input("Enter your name:")
Pname=input("Enter your partner's Name:")
cname=Yname+Pname
cname=cname.lower()
t=cname.count('t')
r=cname.count('r')
u=cname.count('u')
e=cname.count('e')
true=t+r+u+e

l=cname.count('l')
o=cname.count('o')
v=cname.count('v')
e=cname.count('e')
love=l+o+v+e

score = int(str(true) + str(love))
if score <10 or score>90:
    print(f"Your love score is {score} and you're going to have blast in love life.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score} and you have a normal love life together.")
else:
    print(f" Your Love Score is {score}.")

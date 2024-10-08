r1=['😃','😃','😃']
r2=['😃','😃','😃']
r3=['😃','😃','😃']
m=[r1,r2,r3]
print(f'{r1}\n{r2}\n{r3}')
print("Matrix:")
for i in range(0,3):
    print(m[i])

pos=input("Enter your position:")
rn=int(pos[0])
cn=int(pos[1])
print(f"{rn},{cn}")
m[rn-1][cn-1]='X'

print("The New Matrix:")
for i in range(0,3):
    print(m[i])

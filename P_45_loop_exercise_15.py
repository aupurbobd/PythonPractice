numbers=input("Enter the numbers separated by comma:")
print(numbers)
number_list=numbers.split(" ")
print(number_list)
max=int(number_list[0])
c=0
for i in number_list:
    c+=1
for i in range(1,c):
    if int(number_list[i])>max:
        max=int(number_list[i])
print(f'The maximum number is {max}')


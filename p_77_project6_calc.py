def calc(num1, num2, op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='/':
        return num1/num2
    elif op=='*':
        return num1*num2


number1=float(input('Enter the first number:'))

wrong_op=True
while wrong_op:
    operator=input('Pick an operator (+, -, /, *):')
    if operator in ('+', '-', '/', '*'):
        wrong_op=False
    else:
        print('Wrong operator!')

number2=float(input('Enter the second number:'))
result=calc(number1,number2,operator)
print(f'{number1} {operator} {number2} = {result}')
proceed =True
while proceed:
    wrong_key=True
    while wrong_key:
        flag=input(f'Enter \'y\' to calculate more with {result} or \'n\' to start new calculation or \'x\' to exit:')
        if flag.lower()=='n':
            result=0
            wrong_key=False
            number1 = float(input('Enter the first number:'))
            wrong_op = True
            while wrong_op:
                operator = float('Pick an operator (+, -, /, *):')
                if operator in ('+', '-', '/', '*'):
                    wrong_op = False
                else:
                    print('Wrong operator!')
            number2 = float(input('Enter the second number:'))
            result = calc(number1, number2, operator)
            print(f'{number1} {operator} {number2} = {result}')
        elif flag.lower()=='x':
            proceed=False
            wrong_key=False
        elif flag.lower()=='y':
            number1=result
            wrong_op = True
            while wrong_op:
                operator = input('Pick an operator (+, -, /, *):')
                if operator in ('+', '-', '/', '*'):
                    wrong_op = False
                else:
                    print('Wrong operator!')
            number2 = float(input('Enter another number:'))
            result = calc(number1, number2, operator)
            print(f'{number1} {operator} {number2} = {result}')
            proceed=True
            wrong_key=False
        else:
            wrong_key=True
            print('Wrong choice!')
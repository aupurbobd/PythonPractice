#calculate if the number is prime

def isPrime(number):
    f=0
    if number ==1:
        f=0
    else:

        for i in range(3,round(number/2,)+1,2):
            if number%i==0:
                break
        else:
            f=1
    return f
def primeNumbers(ranges):
    primes=[2]
    for i in range(3,ranges+1,2):
        f=0
        for j in range(3,round(i/2)+1,2):
            if i%j==0:
                break
        else:
            f=1
        if f==1:
            primes.append(i)
    return primes

number=int(input("Enter a number:"))
if isPrime(number)==1:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')

p=primeNumbers(number)
print(p)


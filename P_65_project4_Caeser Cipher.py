alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text, shifkey):
    ciphertext=''
    for letter in text:
        if letter in alphabets:
            position=alphabets.index(letter)
            position=position+shifkey
            if position<0:
                position=position+26
            position=position%26
            ciphertext=ciphertext+alphabets[position]
        else:
            ciphertext=ciphertext+letter
    return ciphertext

flag='yes'
while flag.upper()=='YES':

    action=input('Type enc for encryption, type dec for decryption:')
    if action.lower()=='enc':
        message = input('Type your message:')
        shift = int(input("Enter the shifting number:"))
        cipheredText = cipher(message.lower(), shift)
        print(f'The encrypted message is: {cipheredText}')
    elif action.lower()=='dec':
        message = input('Type your message:')
        shift = int(input("Enter the shifting number:"))
        shift = shift * -1
        cipheredText = cipher(message.lower(), shift)
        print(f'The decrypted message is: {cipheredText}')
    else:
        print('Wrong choice!')

    flag=input('Do you want to continue?(yes/no):')
print('Goodbye')
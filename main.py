from string import digits, punctuation, ascii_letters
from random import choice
import sys

def gen(string):
    password = []
    string = [str(x) for x in string]
    for _ in range(length):
        password.append(choice(string))
    password = ''.join(password)
    print('Password:', password)

def main(ispunc):
    if ispunc == 'yes' or ispunc == 'Yes' or ispunc == 'YES':
        string = digits + punctuation + ascii_letters
        gen(string)
    elif ispunc == 'no' or ispunc == 'No' or ispunc == 'NO' or ispunc == 'nO':
        string = digits + ascii_letters
        gen(string)
    else:
        print('There is no [{}] command. Try again.'.format(ispunc))

if __name__ == '__main__':
    while True:
        try:
            length = int(input('Set length of password (0 to exit): '))
            if length == 0:
                break
            ispunc = input('Use spec-symbols? (yes/no): ')
            main(ispunc)
        except:
            pass
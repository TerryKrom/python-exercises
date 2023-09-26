# Let's verify if a word is a palindrome

def palindrome_check(str):
    reversedString = str[::-1]
    if(str == reversedString):
        print('Its a palindrome! ')
    else:
        print('Is not a palindrome! ')


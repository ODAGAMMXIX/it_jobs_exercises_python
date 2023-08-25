def is_palindrome(word):
    word = word.lower()
    length = len(word)          # i:de 0 aa 2 ??? length:5
    for i in range(length // 2):#// operator performs the division 
                                #and then rounds the result down to the nearest integer, 
                                #effectively removing the decimal portion.
                                #RADAR
                                #01234
        if word[i] != word[length - 1 - i]: 
            return False
    return True

def main():
    # Read the input word from the user
    word = input("Enter a word: ")
    #CONSIGO TESTAR ESSE MÉTODO?
    # Check if the word is a palindrome
    if is_palindrome(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")

if __name__ == '__main__':
    main()
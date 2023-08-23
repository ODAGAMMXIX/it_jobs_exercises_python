def is_palindrome(word):
    word = word.lower()  # Convert the word to lowercase for case-insensitive comparison
    return word == word[::-1] #Python's slicing notation to create a reversed version of the word


############
def main():#
############
    # Read the input word from the user
    word = input("Enter a word: ")
    # Check if the word is a palindrome
    if is_palindrome(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")


###########################
if __name__ == '__main__':#
    main()                #
###########################

def is_palindrome(word):
    word = word.lower()
    length = len(word)
    for i in range(length // 2): #// operator performs the division 
                                #and then rounds the result down to the nearest integer, 
                                #effectively removing the decimal portion.
        if word[i] != word[length - 1 - i]:
            return False
    return True

# Read the input word from the user
word = input("Enter a word: ")

# Check if the word is a palindrome
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")

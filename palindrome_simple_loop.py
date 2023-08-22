def is_palindrome(word):
    word = word.lower()
    length = len(word)
    
    for i in range(length):
        if word[i] != word[length - i - 1]:
            return False
    return True

# Read the input word from the user
word = input("Enter a word: ")

# Check if the word is a palindrome
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")

#n this version of the code, 
# we use a loop to iterate through
#  the characters of the word. 
# The loop variable i starts from 0 and goes up to length - 1.
#  We compare the characters at index i and length - i - 1
#  to check for palindromes. 
# If the characters are not equal at any point, we return False.
#  If the loop completes without finding a mismatch, 
# we return True, indicating that the word is a palindrome.
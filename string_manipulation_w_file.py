def main():
    # Read a string from the user
    input_string = input("Enter a string: ")

    # String manipulation techniques
    input("Press Enter to see the uppercase string...")
    uppercase_string = input_string.upper()
    print(f"Uppercase String: {uppercase_string}")

    input("Press Enter to see the reversed string...")
    reversed_string = input_string[::-1]
    print(f"Reversed String: {reversed_string}")

    input("Press Enter to see the word list...")
    word_list = input_string.split()
    print(f"Word List: {word_list}")

    # Write the string to a file
    input("Press Enter to write the output to a file...")
    with open('output.txt', 'w') as file:
        file.write(f"Original String: {input_string}\n")
        file.write(f"Uppercase String: {uppercase_string}\n")
        file.write(f"Reversed String: {reversed_string}\n")
        file.write(f"Word List: {word_list}\n")

    # Read the file and print each character with its position
    input("Press Enter to read the file and print characters...")
    with open('output.txt', 'r') as file:
                          #########################
        for index, char in enumerate(file.read()):#
                          #########################
            print(f"Position {index}: '{char}'")

if __name__ == '__main__':
    main()

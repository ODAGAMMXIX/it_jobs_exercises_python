def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #"recursion" = 5x4x3x2x1

#Print the sequence of multiplication steps
def print_factorial_sequence(n):
    sequence = " x ".join(str(i) for i in range(n, 0, -1))
    print(f"The sequence: {sequence}")
    return f"The sequence: {sequence}"
 

def main():
    # Read the input number from the user
    given_number = int(input("Enter a number: "))

    # Calculate the factorial
    calculated_result = factorial(given_number)

    # Print the factorial result
    print(f"The factorial of {given_number} is {calculated_result}")

    print_factorial_sequence(given_number)

if __name__ == '__main__':
    main()

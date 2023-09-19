
def factorial(n):
    result = 1
    for i in range(1, n + 1):#from 1 to 6: 1x1x2x3x4x5
        result *= i
    return result

# Read the input number from the user
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the factorial result
print(f"The factorial of {num} is {result}")

# Print the sequence of multiplication steps
def print_factorial_sequence(n):
    sequence = " x ".join(str(i) for i in range(1, n + 1))
    print(f"The sequence: {sequence}") #why not 1x1x2x3x4x5? instead 1x2x3x4x5

print_factorial_sequence(num)

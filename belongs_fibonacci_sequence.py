def is_perfect_square(n):
    sqrt = int(n ** 0.5)
    return n == sqrt * sqrt

def is_fibonacci_number(n):
    if n == 0 or n == 1:
        return True
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def fibonacci_sequence_up_to_number(target):
    sequence = []
    i = 0
    while True:
        fib = fibonacci(i)
        if fib <= target:
            sequence.append(fib)
        else:
            break
        i += 1
    return sequence

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    target_number = int(input("Enter a number: "))
    
    if is_fibonacci_number(target_number):
        print(f"{target_number} belongs to the Fibonacci sequence.")
        sequence = fibonacci_sequence_up_to_number(target_number)
    else:
        print(f"{target_number} does not belong to the Fibonacci sequence.")
        next_fib = next_fibonacci_number_after(target_number)
        sequence = fibonacci_sequence_up_to_number(next_fib)
    
    print("Fibonacci sequence:")
    print(sequence)

def next_fibonacci_number_after(n):
    i = 0
    while True:
        fib = fibonacci(i)
        if fib > n:
            return fib
        i += 1

if __name__ == '__main__':
    main()

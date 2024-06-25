#Write a Python program to print first n Fibonacci numbers

#The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it. Starting from 0 and 1, the sequence is:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(n):
    # Initialize the first two Fibonacci numbers and the sequence list
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n terms
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence[:n]

# Take the number of terms input from the user
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

# Check for non-positive input
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    # Get the Fibonacci sequence
    fib_sequence = fibonacci(num_terms)
    
    # Print the Fibonacci sequence
    print(f"The first {num_terms} Fibonacci numbers are: {fib_sequence}")

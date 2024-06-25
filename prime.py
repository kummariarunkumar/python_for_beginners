#Write a Python program to check the given number is prime number or not.
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # Other even numbers are not prime

    # Check divisibility from 3 to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False  # Number is divisible by i, so it is not prime
    return True  # Number is prime

# Take number input from the user
num = int(input("Enter a number: "))

# Check if the given number is a prime number
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

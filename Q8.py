# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print(f"The factors of{x}are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Ënter a number :"))

print_factors(num)

# To find LCM

'''
This code defines a function `compute_lcm` to calculate the Least Common Multiple (LCM) of two numbers. Here's a step-by-step breakdown:

1. The function `compute_lcm` takes two arguments, `x` and `y`.
2. It determines the greater of the two numbers and assigns it to the variable `greater`.
3. It then enters an infinite loop (`while True:`) and checks if the current value of `greater` is divisible by both `x` and `y`.
4. If `greater` is divisible by both, it assigns this value to `lcm` and breaks the loop.
5. If not, it increments `greater` by 1 and checks again.
6. Finally, it returns the value of `lcm`.

The user inputs two numbers, and the LCM of these two numbers is computed and printed.
Here's how it works:

1. It asks the user to input two numbers.
2. It computes the LCM of these two numbers using the `compute_lcm` function.
3. It prints the result.

The code works correctly for finding the LCM.
'''
def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y

    while True:
        if greater %x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm

num1=int(input("Enter any number for x: "))
num2=int(input("Enter any number for y: "))

print(f" The Lcm of {num1} and {num2} is :{compute_lcm(num1,num2)}")




'''
 However, there are more efficient ways to find the LCM using the relationship between GCD (Greatest Common Divisor) and LCM.
    Here's an optimized version using this method:
    This version leverages Python's `math.gcd` function to calculate the LCM more efficiently.
'''
import math

def compute_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

num1 = int(input("Enter any number for x: "))
num2 = int(input("Enter any number for y: "))

print(f"The LCM of {num1} and {num2} is: {compute_lcm(num1, num2)}")





# if it is a multiply of 3 display of zip using range()

def check_multiple(number):
    if number % 3 == 0:
        return "Zip"
    else:
        return number

# Test the function with a range of numbers
for i in range(1, 21):
    print(check_multiple(i))

#Taking input from user using input()
  
# if it is a multiply of 3 display of zip using input()
def check_multiple(number):
    if number % 3 == 0:
        return "Zip"
    else:
        return number

# Take input from the user
try:
    user_input = int(input("Enter a number: "))
    print(check_multiple(user_input))
except ValueError:
    print("Please enter a valid integer.")

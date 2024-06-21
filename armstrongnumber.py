#write a program to check armstrong number?
#It is a number that is equal to the sum of its own digits, each raised to a power equal to the number of digits in the number.
num= int(input("Enter a number: "))
num_str=str(num)
num_digits=len(num_str)

sum_of_powers=0
temp_num= num

while temp_num > 0:
    digit=temp_num % 10
    sum_of_powers +=digit ** num_digits
    temp_num //=10

if sum_of_powers == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not a arm strong number")

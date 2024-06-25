#Write a Python program to check whether the given year is leap year or not.

def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is also divisible by 400
            if year % 400 == 0:
                return True  # Year is divisible by 400, so it is a leap year
            else:
                return False  # Year is divisible by 100 but not by 400, so it is not a leap year
        else:
            return True  # Year is divisible by 4 but not by 100, so it is a leap year
    else:
        return False  # Year is not divisible by 4, so it is not a leap year

# Test cases
test_years = [1900, 2000, 2004, 2019, 2020, 2100, 2400]

for year in test_years:
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


#TAKINKG INPUT FROM USER USING input()
def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is also divisible by 400
            if year % 400 == 0:
                return True  # Year is divisible by 400, so it is a leap year
            else:
                return False  # Year is divisible by 100 but not by 400, so it is not a leap year
        else:
            return True  # Year is divisible by 4 but not by 100, so it is a leap year
    else:
        return False  # Year is not divisible by 4, so it is not a leap year

# Take year input from user
year = int(input("Enter a year: "))

# Check if the given year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


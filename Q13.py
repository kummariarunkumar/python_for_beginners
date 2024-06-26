
#Python Program to Count the Number of Occurrence of a Character in String

count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)

'''
In the above example, we have found the count of 'r' in 'Programiz'. 
The for-loop loops over each character of my_string and the if condition checks if each character of my_string is 'r'. 
The value of count increases if there is a match.
'''

#Example 2: Using method count()

my_string = "Programiz"
my_char = "r"

print(my_string.count(my_char)) #count() counts the frequency of the character passed as parameter.


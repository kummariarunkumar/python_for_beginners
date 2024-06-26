from enum import Enum   #This line imports the Enum class from the enum module. 
                        #The Enum class is used to create enumerations, which are a set of symbolic names bound to unique, 
                        # constant values.

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

# print the enum member
print(Day.MONDAY)

# get the name of the enum member
print(Day.MONDAY.name)

# get the value of the enum member
print(Day.MONDAY.value)
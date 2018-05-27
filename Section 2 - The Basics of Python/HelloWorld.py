# Section 5, Lecture 23 - Getting To Know Python
# Metadata (Project description)
__author__ = 'Nhat Nguyen'

# Values go inside the parentheses
# Strings can be enclosed in either single or double quotes
# The quotes must be the same type (Beginning and End)
print('Hello World!')

# print() prints the string representation of
# the object to the console
print(1 + 2)
print(7 * 5)
print("The End")
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')

# Joins the Strings together
print("hello" + " world")

# Store Strings in variables
greeting = "Hello"
name = "Bruce"
print(greeting + name)
print(greeting + " " + name)

# Hash symbol makes comments in Python

# Note: Using Java before, I will use double quotes for Strings
# It is to be noted that most Python programmers use single
# Because it is easier to type without using the shift key

# Section 5, Lecture 24 - Understanding More About Python
greeting = "Hello"
# input() is a built-in function that read the user input
# and converts to String
name = input("Please enter your name ")
print(greeting + " " + name)

# /n creates a new line
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# Note: Ctrl + / will commit out code

# \t create a new tab
tabbedString = "1\t2\t3\t4\t5\t"
print(tabbedString)

# \" creates double quotes and works with single quotes
print('The pet shop owner said "No, no, \'e\'s uh,....he\s resting"')
print("The pet shop owner said \"No, no, 'e's uh,....he's resting\"")

anotherSplitString = """This string has been
split over
several lines"""
print(anotherSplitString)

# Triple quotes Example
print('''The pet shop owner said "No, no, 'e's' uh,...he's resting"''')
print("""The pet shop owner said "No, no, 'e's' uh,...he's resting" """)

# Quiz 3: Printing Tabs
print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")

# Section 5, Lecture 25 - Storing Items In Variables
# Variables: variable name gets referred to an area of memory to find stored values
greeting = "Bruce"
_myName = "Tim"
Tim45 = "Good"
Tim_Was_57 = "Hello"
Greating = "There"

# Variable name must start with a letter or underscore
# Greeting and greeting are different

print(Tim_Was_57 + " " + greeting)

age = 24
print(age)

# print(greeting + age) creates an error
# because cannot concatenate String and number

# Python has data types classified as numerics, sequences,
# mappings, files, classes, instances, and exceptions
# String is a sequence type
# Integer is a whole number (no decimal point)
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# / returns as a float
print(a / b)
# // returns as a integer
print(a // b)
print(a % b)

# I understand Java so I won't struggle with this
# but a common error is giving float when it need an integer value
# Note: a/b will not work because it is a float when it needs int
for i in range(1, a//b):
    print(i)

print(a + b / 3 - 4 * 12)
# Make code unambiguous
print(8 / 2 * 3)
print(8 * 3 / 2)

print(((((a+b) / 3) - 4) * 12))

# Quiz 4: Integer Division
bun_price = 2.40
money = 15
print(money // bun_price)

# Section 5, Lecture 26 -  More About Variables And Strings
# Operator Precedence is basically the
# computer way of order of operations

c = a + b
d = c / 3
e = d - 4
print(e * 12)

# At this point I recommend looking up all
# Python data types and know the core ones

# String data type
parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[2])
# print(parrot[14]) will be an error because it is out of range
# -1 count backwards
print(parrot[-1])
# The 6th letter is not included
print(parrot[0:6])
# Beginning to 6th letter
print(parrot[:6])
# 6th letter to end
print(parrot[6:])
# Counting backwards
print(parrot[-4:-2])
# Skip 1 letters
print(parrot[0:6:2])

number = "9,223,372,036,854,775,807"
# From 1st to end skipping 3 letters
print(number[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
# From beginning to end skipping 2 indexes
print(numbers[0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
# This works
print("he's" "probably" "pining")
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")
today = "friday"
# Searches word within string, return boolean
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in today)

# Section 5, Lecture 27 -  String Formatting - Displaying Numbers And Strings
age = 24
# Cannot add int and strings so use str method
print("My age is " + str(age) + " years")

# Replacement Field Example
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} "
      .format(31, "January", "March", "May", "July", "August", "October", "December"))

# Useful in this example
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# Replacement value based on data type
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

# Two stars means raising the power
for i in range(1, 12):
    print("No. %2d squared is %3d and cubed is %4d" % (i, i ** 2, i ** 3))

# %12.50 is formatting number 50 means placement after decimal point
print("Pi is approximately %12.50f" % (22 / 7))

# Replacement Field Example 2 - {1:3} is {index:space}
for i in range(1, 12):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# Replacement Field Example 3
print("Pi is approximately {0:12.50}".format(22 / 7))

# Replacement Field can be used many times

# Automatically place the index values when blank 1, 2, 3
for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
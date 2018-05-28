__author__ = "Nhat Nguyen"

# Lecture 29 - An Introduction To Program Flow Control

# For Loop Example
# Indentation is important in Python
# When indented, it is part of of the code block
# Python does not have delimiters like Java {}
for i in range(1, 12):
    print("No {} squared is {:2} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("Calculation complete")
    print("Try again")

# Do not mix spaces and tabs when indenting blocks

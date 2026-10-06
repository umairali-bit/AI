# Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

raw_input = input("Please enter comma separated numbers: ")
l = raw_input.split(",")
t = tuple(l)
print(l)
print(t)


# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InputOutStr(str):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Please enter s string: ")
        return self.s

    def printString(self):
        print(self.s.upper())


str_obj = InputOutStr()
str_obj.getString()
str_obj.printString()


# Write a program that calculates and prints the value according to the given formula:
#
# Q = Square root of [(2 _ C _ D)/H]
#
# Following are the fixed values of C and H:
#
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:

from math import sqrt

c = 50
h = 30

def calc(d):
    return sqrt((2*c*d)/h)

d = input().split(",")
d = [str(round(calc(int(i)))) for i in d]
print(d)
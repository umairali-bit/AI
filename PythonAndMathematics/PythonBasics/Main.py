from datetime import date

#name = input('What is your name? ')
#print('Hello ' + name)

#Fundamental Data Types
int
float
bool
str
list
tuple
set
dict


#Classes -> custom types
#SuperCar

#Specialized Data Types
#Modules

None # ->  means nothing like zero


int # A number
print(type(2 + 4)) #type shows the data type

float
print(type(20+1.0))

print (2 ** 2) # = 4 its 2 to the power of 2
print (7 / 2) # = 3.5
print (7 // 2) # = 3 Floor division returns the integer part after rounding down.

#math functions
print(round(3.1)) #3
print(abs(-20)) #20


#Complex is for complex math problems

#Binary representation
print(bin(5))
#returning binary into int
print(int('0b101', 2))

#Python variables
#stores information
iq = 190
print(iq)
user_iq = 190 # snake case
_user_iq = 190 # a variable can start with lower case or underscore
#variables are case-sensitive
#don't overwrite variables - print(print)

#Constants are in capitals
PI = 3.14 # this value should never change
a,b,c = 1,2,3
print(a)
print(b)
print(c)

#Expressions vs statement
iq = 100
user_age = iq / 5 #iq / 5 is an expression
user_ages = iq / 5 # this whole line is an expression

# augmented assignment operator
some_user = 5
some_user += 2
some_user -= 2
some_user *= 2
print(some_user)

# Strings
print(type('Hello there!'))
userName = 'user123'
password = 'pass'
long_string = '''

WOW

O O
___

'''

print(long_string)
first_name = 'Walter'
last_name = 'White'
full_name = first_name + ' ' + last_name
print(full_name)

# Type conversion
print(type(int(str(100))))

#Escape Sequence
weather = '\tIt\'s \"kind of\" a sunny day \n hope you have a good day'
print(weather)

#formatted strings

name = "Hank"
age = 50
print(f'Hi {name}. You are {age} years old')
print('Hi {1}. You are {0} years old'.format(name, age))
print('Hi {new_name}. You are {age} years old'.format(new_name = 'gus' , age = 40))

#String indexes
selfish = '01234567'
#[start:stop:stepOver]
print(selfish[0])
print(selfish[0:4])
print(selfish[:5])
print(selfish[1:])
print(selfish[:])
print(selfish[::2])
print(selfish[1::2])
print(selfish[::-1])
print(selfish[-1])


#Built-in functions and methods in Python
greet = 'helloooooooo'
print(len(greet))
print(greet[0])
print(greet[0:len(greet)])
print(greet[1:len(greet)])
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))

#booleans
name = 'Umair'
is_cool = False
is_cool = True

print(bool(1)) #True
print(bool(0)) #False

#exercise
# birth_year = int(input('What year were you born?'))
#
# age = date.today().year - birth_year
#
# print(f'Your age is {age}' )

#Password checker exercise
# user_name = input('What is your user name?')
# password = input('What is your password?')
#
# print(f"Your password {'*' * len(password)} is {len(password)} characters long")

#list - ordered sequence of objects
li = [1,2,3,4,5,6]
li2 = ['a','b','c','d','e','f']
li3 = [1,2,3,'a','b','c', True]

amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[1])

#list slicing

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes']

print(amazon_cart)
print(amazon_cart[0:2]) #start is included but end is included

#lists are mutable
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)


#Matrix is a way to describe multidimensional lists
#2-dimensional array
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) #2










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

#Lists methods

basket = [1,2,3,4,5]
#adding
# new_basket = basket.append(100) because these built in methods (adding, removing) just change the list, doesnt return anything"
# print(new_basket) # none

basket.append(100)
new_basket = basket
print(basket)
print(len(basket))

basket.insert(0,200)
print(basket)

basket.extend([100,200,300])
print(basket)

#removing methods
basket.pop() #removes the last element in the list
basket.pop(2) #removes the element at the index 2 - pop method could return a result
new_basket = basket.pop(3)
print(new_basket)
basket.remove(100) #removes the value at the index
print(basket)

basket.clear()
print(basket)

basket = ['a','b','c','d','e','f','d']
print(basket.index('d')) #3
#index finding with start and stop
print(basket.index('b', 0,5)) #1
#boolean
print ('c' in basket) #true
print('e' in 'Python is easy') #true
print(basket.count('f')) #1

# basket.sort()
print(sorted(basket)) #produces a new list
print(basket)

copy_list = basket.copy()
print(copy_list)

basket.sort()
basket.reverse()
print(basket)
print(basket[::-1]) #reverse again

#create a new list from 1 to 100
print(list(range(0,101)))

#.join
sentence = '!'
sentence.join(['hi', 'my', 'name', 'is', 'Walter', 'White'])
print(sentence) #prints out a space

new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Walter', 'White'])
print(new_sentence)

better_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Walter', 'White'])
print(better_sentence)

#list_unpacking
a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a) #1
print(b) #2
print(c) #3
print(other) #[4,5,6,7,8,9]

#dictionary - the unordered key value pair
dictionary = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}

print(dictionary)

dictionary = {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
}
print(dictionary['b'][3]) #l

my_list = [
    {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
},
    {
    'a': [5,6,7],
    'b': 'hello',
    'x': False
    }
]

print(my_list[1]['x']) # false

#dictionary keys - need to be immutable, unique
dictionary = {
    123:[1,2,3],
    True: 'Hello',

}
print(dictionary[True])

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
print(user['basket'])
print(user.get('greet'))
print('basket' in user) #true
print(user.get('age', 55)) #55. age doesn't exist in user, and we are assigning a default value
print('greet' in user.keys())
print('hello' in user.values())
print(user.items())
# user.clear()
# print(user)
user2 = user.copy()
print(user2)

user2.popitem()
print(user2)

user2.update({'age' : 55})
print(user2)

user3 = dict(name='Jessie Pinkman')
print(user3) #{'name': 'Jessie Pinkman'}

#Tuple - an immutable list
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[3]) #4
print(5 in my_tuple)# true

new_tuple = my_tuple[1:4]
print (new_tuple)
print(new_tuple.count(3)) #1
print(new_tuple.index(4)) #2
print(len(new_tuple))

#sets -unordered collection of unique sets

my_set = {1,2,3,4,5,5}
print(my_set) #{1, 2, 3, 4, 5} returns only unique set
my_set.add(100)
my_set.add(2)
print(my_set) #{1, 2, 3, 4, 5, 100} because 2 already exists in our set

# print(my_set[0])# set does not support indexing
print (1 in my_set)

my_list = [1,2,3,4,5]
print(set(my_list)) #converted list to a set

your_set = {4,5,6,7,8,9,10}
set_set = {1,2,3,4,5,6}

# set_set.difference(your_set)
#
# set_set.discard(5)
# print(set_set)
#
# set_set.difference_update(your_set)
# print(set_set) #removes the common elements between two sets

# print(set_set.intersection(your_set)) #{4, 5, 6}

# print(your_set.isdisjoint(set_set)) #False, they have common elements

# print (set_set.union(your_set)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print (set_set | your_set) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# print(set_set.issubset(your_set)) #False
# print(set_set.issuperset(your_set)) #False









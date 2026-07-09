#Conditional Logic
from email.mime import image
from operator import truediv

is_old = True
is_licensed = False

if is_old:
    print("You are old enough to drive!")
elif is_licensed:
    print("You can drive now!")
else:
    print("You are not of age")

print("okok")

if is_old and is_licensed:
    print("You are old enough to drive!")
else:
    print("You are not of age")


#Truthy Falsey
is_truthy = "Helllloooo"
is_truth = 5

print(bool('Helloooo')) #true
print(bool(5)) #true

print(bool('')) #false
print(bool(0)) #false


password = '123'
user_name = "Hank"

if password and user_name:
    print("You are logged in!")

#Ternary operator
# condition_if_true if condition else condition_if_false
is_friend = True
can_message = "message allowed" if is_friend else "message denied"

print(can_message)

#short-circuiting
is_Friend = True
is_User = True

if is_Friend or is_User:
    print("Best friends forever")

#Logical operators
print( 4 > 5)
print( 4 < 5)
# print ( 4 = 5) # false
print ( 'hellooo' == 'hellooo')
print ('a' > 'A')
print( 0 <= 0)
print ( 0 != 0)
print(not(True))

#Conditional logic exercise
is_Magician = False
is_Expert = True

# check if master AND magician, "You are a master magician"
# check if magician but not the expert. "You are getting there!"
# if not are not magician "You need magical powers"

if is_Magician and is_Expert:
    print("You are a master magician!")
elif is_Magician and not is_Expert:
    print("You are getting there!")
elif not is_Magician:
    print("You need magic powers")

#is vs ==
# == checks whether two objects have equal values.
# is checks whether two variables refer to the exact same object in memory.
print(True == 1)
print('1' == 1)
print([] == [])
print([1, 2, 3] == [1, 2, 3])

print(True is 1)
print('1' is 1)
print([] is [])
print([1, 2, 3] is [1, 2, 3])

# for loop
for items in "I am not in danger, Skyler. I am the danger.":
    print(items)

for item in [1, 2, 3]:
    print(item)
    print(item)
    print(item)

for item in [1, 2, 3]:
    for x in ['a', 'b', 'c']:
        print(item, x)


# iterables

user = {
    'name' : 'Tuco Salamanca',
    'age' : 45,
    'can_Cook' : False
}

for x in user.items():
    print(x)

for x in user.keys():
    print(x)

for x in user.values():
    print(x)

for key, value in user.items():
    print(key, value)


#looping exercise
my_list = [1,2,3,4,5,6,7,8,9,10]
result = 0

for counter in my_list:
    result += counter
print(result)

#range
for number in range(1, 11):
    print(number)

for _ in range(1, 11):
    print(_)

for _ in range(1, 11):
    print(_)

for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

for number in range(1, 11):
    print('email list')

for _ in range(2):
    print(list(range(10)))


# enumerate

for (item, items) in enumerate([1, 2, 3]):
    print(item, items)

for i, char in enumerate('Hellooooooo'):
    print(i, char)


for i, char in enumerate(list(range(100))):
    if char == 50:
        print (f'index of 50: {i}')


#While loop

i = 0
while i < 50:

    print(i)
    i += 1

else:
    print("done with all the work")


my_list = [1,2,3,4,5,6,7,8,9,10]
for item in my_list:
    print(item)

i=0
while i < len(my_list):
    print(my_list[i])
    i += 1

# while True:
#     # resp = input('say something:')
#
#     if resp == 'bye':
#         break
#


#image

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end =' ')
        else:
            print(' ', end =' ')

    print(' ')


# find duplicates

some_list = ['a','b','b','c','d','e','f']
duplicate = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)

print(duplicate)

#Functions

def say_hello():
    print('hellllooooooo')

say_hello()

#Parameters and Arguments
#parameters
def say_hello(name, emoji):
    print(f'hellooooo {name} {emoji}')

#arguments, positional arguments
say_hello('Umair', '😊')

#key_word argument
say_hello(name='Bibi', emoji='❤️')

#default parameters
def say_hello(name='Walter White', emoji='😈'):
    print(f'hello {name} {emoji}')

say_hello()

#return statement
# def sum(num1, num2):
#     print('hiiii')
#     return num1 + num2
#
# total = sum(1,2)
# print(sum(10, total))

# # def sum(num1, num2):
#     def another_func(n1,n2):
#         return n1 + n2
#     return another_func(num1, num2)

# total = sum(1,2)
# print(total)

# func exercise
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()
checkDriverAge(52)
checkDriverAge(12)
checkDriverAge(18)

#DocStrings
def test(a):
    '''
    :param a:
    :return:
    '''

    print(a)

help(test)
print(test.__doc__)

#clean_code
def is_even(num):
    return num % 2 == 0

print(is_even(6))

# *args **kwargs

def super_fuc(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_fuc(1,2,3,4,5, num1=5, num2=10))
#Rule: order -> params, *args, default parameters, **kwargs

#exercise - find the highest even number
def highest_even(li):

    evens = []

    for item in li:
        if item % 2 == 0:
            evens.append(item)
    # return max(evens) - python built in max function


   # manually going through evens
    highest = evens[0]
    for item in evens:
        if item > highest:
            highest = item

    return highest


print(highest_even([10,2,3,4,5,6,7,8,9,20]))

#walrus operator

a = 'helllooooooooooo'
if (n:= len(a)) > 10:
    print(f'too long to print {n}')

while ((n:= len(a)) > 1):

    print(n)

    a = a[:-1]
print(a)

# scope rules
#1 - start with local
a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

#2 - check if parent local?

a = 1

def parent():
    a = 10
    def confusions():
        return a
    return confusions()

print(parent())

#3 check global
a = 1

def parent():
    def confusions():
        return a
    return confusions()

print(parent())

#4 built in python functions

a = 1

def parent():
    def confusions():
        return sum
    return confusions()

print(parent())











































#Conditional Logic
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


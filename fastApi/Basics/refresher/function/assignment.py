# - Create a function that takes in 3 parameters(firstname, lastname, age) and
#
# returns a dictionary based on those values

def display_dictionary(firstname, lastname, age):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'age': age
    }

print(display_dictionary(firstname="John", lastname="Smith", age=20))
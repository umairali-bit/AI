#Decorator
import time


def my_decorator(func):
    def wrap_function():
     print('******')
     func()
     print('******')
    return wrap_function


@my_decorator
def greet():
    print('Hello World')


greet()

def your_decorator(func):
    def wrap_function(x):
        print('******')
        func(x)
        print('******')
    return wrap_function

@your_decorator
def hello(greet):
    print(greet)

hello('hiiiiiiii')

#example

def performance(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end - start} ms')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100):
        i*5

long_time()


user1 = {
    'name' : 'umair',
    'valid': False,
}

def authenticated_user(fn):
    def wrapper(*args, **kwargs):
        if user1['valid']:
            return fn(*args, **kwargs)
        else:
            return 'invalid user'

    return wrapper

@authenticated_user
def message_sent(user):
    print('The message has been sent.')





message_sent(user1)
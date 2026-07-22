#OOP
from abc import abstractmethod, ABC


class MyClass:
    pass

obj = MyClass()

print(type(None))
print(type(False))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type({}))
print(type(()))
print(obj)

#OOP
class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy')
player1.attack = 50
print(player1.name)
print(player1.attack)
print(player1.run())

#exercise cats everywhere - find the oldest cat
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def oldest_cat(cat1, cat2, cat3):

    oldest = cat1

    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3

    return oldest

def oldest_cat2(*args):
    return max(args)

cat1 = Cat('Nova', 8)
cat2 = Cat('Oliver', 5)
cat3 = Cat('Shadow', 4)

oldest = oldest_cat(cat1, cat2, cat3)

print(oldest.name, oldest.age)
print(f'Another way to find the max age is: {oldest_cat2(cat1.age, cat2.age, cat3.age)}')


# class methods
class Dog:

    species = 'dog'

    @classmethod
    def get_species(cls, name):
        return f'{name} is a {cls.species}'

print(Dog.get_species('Zacky'))

#static methods
class Add:

    @staticmethod
    def add(a, b):
        return a + b

print(Add.add(1, 2))

#4 pillars of OOP
#1 Encapsulation
#2 Abstraction

class Tree:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def grow(self):
        return f'{self._name} has an age of {self._age} years in average'

    def length(self):
        return f'{self._name} is usually {self._height} ft tall'

tree = Tree('Anwar ritol', 40, 20)
print(tree.grow())
print(tree.length())
print(tree._name)

#3 inheritance
class User(ABC):
    def sign_in(self):
        return 'signed in'

    @abstractmethod
    def introduce(self):
        pass

class Student(User):
    def __init__(self, name, age):
        self._name = name
        self._age = age


    def introduce(self):
        return f"Student {self._name} is {self.sign_in()} and the student's age is {self._age} years old."

class Teacher(User):
    def __init__(self, name, age, subject):
        self._name = name
        self._age = age
        self._subject = subject


    def introduce(self):
        return f'Teacher {self._name} is {self.sign_in()} and teaching {self._subject}'


student = Student('Jessie Pinkman', 20)
print(student.introduce())

teacher = Teacher('Walter White', 57, 'chemistry')
print(teacher.introduce())

#isinstance
print(isinstance(student, Student)) #true
print(isinstance(teacher, object)) #true

#polymorphism

def in_class(user):
    return user.introduce()

print(in_class(student))
print(in_class(teacher))

#pet exercise

# Exercise Pets Everywhere

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Oliver(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats =[Simon(Simon, 5), Sally(Sally, 4), Oliver(Oliver, 6)]

my_pets = Pets(my_cats)

my_pets.walk()

#Super()
class Employee:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email

    def signin(self):
        return 'signed in'


class Manager(Employee):
    def __init__(self, name, age, email):
        super().__init__( name, age, email)

    def work(self):
       return f'Manager {self._name} is {self._age} years old, and his email is {self._email}. He is {self.signin()}.'

Manager1 = Manager(name='Gus Fringe', age=57, email = 'gus@unknown.com')
print(Manager1.work())
# introspection
print(dir(Manager1.work()))


# dunder methods
class Money:
    def __init__(self, amount):
        self._amount = amount

    def add(self, other):
       return Money(self._amount + other._amount)

    def __str__(self):
        return str(self._amount)

a = Money(10)
b = Money(20)

print(a.add(b))

#exercise

class SuperList(list):
    def __len__(self):
        return 1000

superList1 = SuperList()
print(len(superList1))
superList1.append(10)
superList1.append(5)
print(superList1[0])
print(superList1[1])
print(issubclass(SuperList, list))

#Multiple inheritance
class Person:
    def introduce(self):
        return 'Hi I am also a person'

class EmailMixin:
    def send_email(self):
        return "Sending email..."

class Engineer(Person, EmailMixin):
    pass

engineer = Engineer()
print(engineer.introduce())
print(engineer.send_email())

#MRO - Method resolution order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.__mro__)






































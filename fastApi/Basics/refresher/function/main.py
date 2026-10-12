# Functions in python

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet('Umair'))

def print_my_name(first_name: str, last_name: str) -> str:
    print(f"Hello, {first_name} {last_name}!")

print_my_name("Umair", "Ali")

def print_color():
    color = 'Red'
    print(f"{color}! is my color")

print_color()

def print_numbers(highest_number, lowest_number):
    print(f"Lowest number is {lowest_number} and highest number is {highest_number}!")

print_numbers(lowest_number=10, highest_number=20)


def buy_item(cost_of_item):
    return cost_of_item + add_tax(cost_of_item)

def add_tax(cost):
    tax = 0.3
    return cost * tax


print(buy_item(2))
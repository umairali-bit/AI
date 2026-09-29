#Error Handling

# while True:
#     try:
#         age = int((input('Please enter your age')))
#         10/age
#     except ValueError:
#         print('Please enter a valid age')
#     except ZeroDivisionError:
#         print('Please enter age higher than 0')
#     else:
#         break

#Error handling example

def sum(num1, num2):

    try:
        return num1 + num2

    except TypeError as err:
        # print(f'Please enter two numbers {err}')
        raise ValueError("Invalid input")

print(sum('10', 20))
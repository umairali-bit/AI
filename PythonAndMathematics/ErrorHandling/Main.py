#Error Handling

while True:
    try:
        age = int((input('Please enter your age')))
        10/age
    except ValueError:
        print('Please enter a valid age')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        break
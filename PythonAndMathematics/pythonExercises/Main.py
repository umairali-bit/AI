# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence
# on a single line.

def main():

    for i in range(2000,3200):
        if i%7 == 0 and i%5 == 0:
            print(i, end =",")
    print("\b")

main()

# Write a program which can compute the factorial of a given number. Suppose the following input is
# supplied to the program: 8 Then, the output should be:40320

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    yield result

gen = factorial(5)

print(next(gen))
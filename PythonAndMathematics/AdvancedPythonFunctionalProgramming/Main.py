from functools import reduce


def multiply_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list

print(multiply_2([1, 2, 3, 4])) #[2, 4, 6, 8]

#map()
my_list = [1, 2, 3, 4]
def multiply_3(item):
    return item * 3

print(list(map(multiply_3, my_list)))
print(my_list)

#filter()
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, [1,2,3,4,5,6,7,8,9,0])))

#zip()
your_list = [10,20,20,40]
print(list(zip(your_list,my_list)))

#reduce()
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator,my_list, 0))


#exercise
#map
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
result = map(str.upper, my_pets)
print(list(result))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(scores):
    return scores > 50

print(list(filter(is_smart_student, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def acc (accs, item):
    return accs + item


print(reduce(acc,(my_numbers + scores)))


#lambda
lambda_list = [10,20,30,40]
print(list(map(lambda item: item*2,lambda_list)))

#exercise - square lambda_list
print(list(map(lambda item: item **2, lambda_list)))

#exercise - sorting the second element in a tuple
a =[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key= lambda item: item[1])
print(a)

#comprehension
my_conventional_list = []

for char in 'hello':
    my_conventional_list.append(char)

print(my_conventional_list)

my_comprehension_list = [char for char in 'hello']
print(my_comprehension_list)

my_comprehension_list2 = [num for num in range(0,100)]
print(my_comprehension_list2)

my_comprehension_list3 = [num*2 for num in range(0,100)]
print(my_comprehension_list3)

my_comprehension_list4 = [num*2 for num in range(0,100) if num % 2 == 0]
print(my_comprehension_list4)

#dictionary
simple_dict = {
    'a' :  1,
    'b' : 2
}

my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)

#exercise
some_list = ['a','b','c','d','e','b', 'd']

duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)




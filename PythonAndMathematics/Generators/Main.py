#Generators

def my_list(num):
    result = []

    for i in range(num):
        result.append(i)
    return result

print(my_list(100))

def generator_func(num):
    for i in range(num):
        yield i

generator = generator_func(100)

# print(next(generator))
# print(next(generator))
# print(next(generator))


#under the hood of Generators
class MyClass:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.first < self.last:
            num = self.first
            self.first += 1
            return num

        raise StopIteration


gen = MyClass(100, 200)
for i in gen:
    print(i)
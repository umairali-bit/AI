

numbers = []
sum_of_numbers = 0

for i in range(0,5):
    numbers.append(i)

print(numbers)

for x in numbers:
    sum_of_numbers += x
print(sum_of_numbers)

j = 0

while j < 5:
    j +=1
    if j == 3:
        continue
    print(j)
else:
    print("Thank you for using this program")


my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
count = 0

while count < 3:
    for day in my_list:
        if day == "Monday":
            continue
        print(day)

    count += 1
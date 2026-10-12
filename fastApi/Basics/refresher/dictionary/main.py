#Dictionary

user_dictionary = {
    "username": "codingMaster",
    "name": "Skyler White",
    "age": 32

}

print(user_dictionary)

print(user_dictionary["name"])
print(user_dictionary.get("name"))
print(user_dictionary.get("age"))
print(user_dictionary["age"])

user_dictionary["married"] = True

print(user_dictionary)

print(len(user_dictionary))

for x in user_dictionary:
    print(x)
    print(user_dictionary[x])

for x, y in user_dictionary.items():
    print(x,y)

user_dictionary2 = user_dictionary
user_dictionary2.pop("age")
print(user_dictionary2)
print(user_dictionary)

user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)
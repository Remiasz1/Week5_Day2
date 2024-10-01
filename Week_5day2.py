# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# Tuple = () ordered and unchangable. Duplicates OK. Faster

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# print("pineapple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits)

# print(fruits[0])
# for fruit in fruits:
#     print(fruit)

# print(fruits[0])
# for fruit in fruits:
#     print(fruit)
# cars = ["FORD", "VOLVO", "BMW"]

# for car in cars: 
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f"The cars in the list area: {cars}")
#     if len(cars) > 10:
#         print("You have reached the maximum number of cars")
#         break


friends = ["Hector"]
friends.append("Victor")
friends.append("Dominik")
friends.append("Gerdo")
print(f"The List of friends are: {friends}")
friends[-1] = "Dom"
###############sets###############
# sets are unordered and unindexed
# they are defined using curly brakcets
# they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# print(fruits)
# print(dir(fruits)) #Method can be used with sets
# print(help(fruits)) #Documentation/methods that caqn be used with sets
# print(len(fruits)) #Number of elements in set
# print("Volve" in fruits) #Checks if an element is in fruits
# print(fruits.add("orange"))
# print (fruits)
# print(fruits.add("kiwi"))
# print(fruits)
#add multiple elements to set
# print(fruits.update(["orange", "kiwi", "pineapple"]))
# print(fruits)
# print(fruits.pop()) #removes the last element in set
# print(fruits)
# print(fruits.clear) #clears set
# print(fruits)
#When to use sets
#Sets are useful when you want to store a
#collection of items that should not be changed
#and you don't care about the order of the items
# social_security_number = {123456789, 2468, 13579}
# remove last element from step
# print(social_security_number.pop())
# print(social_security_number)
# add more
# print(social_security_number.add(123789))
# print(social_security_number)

#####################uples####################
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2))
# #Counts number of times 2 is in set
# print(dir(example_tuple))
# #methods thac be used with set
# print(help(example_tuple))
# #Documentation/methods in tuple
# print(len(example_tuple))
# #number of elements in a tuple
# print(2 in example_tuple)
# #checks if element is in tuple
# #Tuples are useful when you want to store a collection of items that should not be changed
# print(example_tuple.index(2))

# lymeric = "peter piper picked a peck of pickled pepper"
# #convert string in tuple
# #split first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# print(lymeric_tuple.count("peck"))
# print(lymeric_tuple.count("peppers"))
# # loop with tuples
# for item in example_tuple:
#     print(item)


#dictonary
#dictonaries are unordered, changeable and index
#defined by curly brakets
# has keys and values
# keys are unique
#values can be any data type
capitals = {"Kenya":"Nairobi",
            "Uganda" : "Kampala",
             "Tanzania" : "dodoma",
              "Rwanda": "Kligali",
               "China": "Bejing",
                "U.S": "Washington D.C."}
print(capitals) 
# #dir, help and len can be used for dictionary
# print(dir(capitals)) # methods that can be used in dictonaries
# print(help(capitals)) # methods/documentation that can be used with dictonaries
# print(lens(capitals)) # Want top check the value of the key in the dictionary
#add an item
capitals.update({"Nigeria": "Abuja", "Spain": "Madrid","Korea": "Seoul"})
print(capitals)
# capital.clear()
# loop through dictionary
for key in capitals:
    print(f"what are in {key}")

# print values in dictionary
for value in capitals.values():
    print(value)
 #print the key value pairs in dictionary
    items_all = capitals.items()
for key, value in items_all:
    print(f"{key} is the capital of {value}")

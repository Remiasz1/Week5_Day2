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
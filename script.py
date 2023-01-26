#containers of colletions of data.  In JS strings are data types.  In Python strings of strings are objects and object are containers. 

#Three types of Python containers: 1. dictionaries - js equivilant is object 2. list -js equivliant is array 3. tuple - no equivilant in js

#Dictionaries - looks just like an object in js

student = {
    "name": "Mark",
    "course": "SEIR",
    "current_week": 22
}

# the syntax for accessing a value in a dictionary is the same as js
#they are mutable- they can be altered, changed, updated, etc.
#when looping through the keys in a dictionary, the order is not guaranteed

#List - looks just like an array in js but there is no dot notation for accessing values in a list but bracket notation does exist


name = student["name"]

print(name)

#get method - if the key does not exist, it will return None
#.get() method

#keys() - returns a list of all the keys in the dictionary
#values() - returns a list of all the values in the dictionary
# #items() - returns a list of tuples of all the key value pairs in the dictionary

# print(student.get("course"))
# print(student.get("birthdate")) #should return none as its not in the containter (dictionary)
# #can chain the .get method for accessing multiple keys
# print(student.get("name").get("current_week"))

where_my_things_are = {
    "desk": "office",
    "car": "garage",
    "laptop": "office",
    "phone": "charger",
    "shoes": "closet"
}
# write a for loop that iterates over the where_my_things_are dictionary and prints out the following:"My <key> is in the <value>"

for key, value in where_my_things_are.items():
    print(f"My {key} is in the {value}")




##### TUPLES ######
#tuples are immutable - they cannot be changed, altered, updated, etc.
#tuples are ordered - they have an order
#tuples are indexed - they have an index
#tuples are iterable - they can be looped over
#tuples are hashable - they can be used as keys in a dictionary
#tuples use parenthesis - they are defined using parenthesis not brackets

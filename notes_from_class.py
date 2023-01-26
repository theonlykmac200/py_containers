# Python Containers

# Dictionaries - Object
# Lists - Array
# Tuples - N/A


# Dictionaries #########################

student = {
    "name": "Fred",
    "course": "SEIR",
    "current_week": {
     "22": True
    }
}

# the syntax is exactly like JS BUT you must wrap the keys in quotes
# they are mutable - they can be altered, changed, added to, removed from
# when looping through an object, the order is random

# There is not dot notation in python

name = student['name'] # use bracket notation to access a key

# print(name)

# .get() method

# birthdate = student["birthdate"]

# print(birthdate)

#print( student.get("birthdate") ) # this will return None

#print( student.get("current_week").get("22") ) # this will return the value just like bracket notation

# You can chain .get() for accessing deeper nested dictionaries

#print( student.get("birthdate", "04-04-1985")) # does not alter the original dict



# In Operator - checks to see if a value is "IN" the iterable

if "course" in student:
    print( f'{student["name"]} is enrolled on {student["course"]}' )
else:
    print( f'{student["name"]} is not enrolled in a course')



# Adding Items 

student["age"] = 21 # use bracket notation


# Deleting Items

del student["age"] # delete the key and value at that location

# print( "age" in student ) # returns False if the key is not present


# Number of items in a Dict use len()

# print( len( student ) )


# Looping through Dictionaries

for key, val in student.items(): # .items() is required to get the key and val for each iteration
    print( f'{key} = {val}')

# student.items() this returns a tuple
# dict_items([("name, "Tina), ("course", "SEI")])


where_my_things_are = {
    "shoes": "in my closet",
    "keys": "in my purse",
    "cheese": "in my fridge"
}

for thing, location in where_my_things_are.items():
    print( f'My {thing} is kept {location}')



# Lists ###########################################

# type is list 
# can contain 0 or more items of any data type

colors = ["red", "blue", "green"]

# to get the length

print( len(colors) )

# lists are a sequence type
# lists are mutable 

idx = 2
colors[idx] # pass in an index number to get the value at that index

# negative numbers can be used to access items from the back of the list

# [0,1,2,3,4,5,6]
# [-7,-6,-5,-4,-3,-2,-1]

# Assigning Items - by index

colors[2] = "purple"


# Adding Items - append()

# add something to the back of the list , does not return

colors.append("green")

# adding multiple items - adds to the end

colors.extend(["orange", "black"])


# Insert items at a specific point

colors.insert(1, "yellow")

# Deleting items - pop() add an index number to be more specific

colors.pop(2) # will remove and return the item at index 2

del colors[3] # will delete the value at index 3

colors.remove("orange") # will remove the first match 

# clear the entire list

# colors.clear() # removes all items from the list


my_colors = colors # changing the original will change the copy

colors.append("teal")

print(my_colors) 

# Looping over lists - Iteration

colors = ['red', 'green', 'blue']

for color in colors:    # you can loop over each and access the value only
    print(color)


for idx, color in enumerate(colors): # you can loop through and access both value and index
    print( idx, color )



# List Comprehension ################################

# <expression> for <item> in <list>


nums = [1,2,3,4,5,6,7,8,9,10]

squares=[]
for num in nums:
    squares.append(num * num)
print(squares)

# I want num x num for each num in nums
# A List comprehension will condense the code above into this
squares = [num * num for num in nums]


# more complex example

nums = [1,2,3,4,5,6,7,8,9,10]

even_squares = []
for num in nums:
    square = num * num
    if square % 2 == 0:
        even_squares.append(square)

# list comprehension for the above code 
# I want num * num for each num in nums if num * num is even
even_squares = [num * num for num in nums if (num * num) % 2 == 0]

# List comprehensions create a new list from a logical statement 


# Tuples ################################################

# Tuples are just like lists 
# type of tuple
# syntax uses parentheses () instead of []
# Tuples are immutable - no changing them

colors = ('red', 'green', 'blue') # this is a tuple

colors = "red", "green", "blue" # this is also a tuple

# they have a len() => 3

hello_tuple = ("hello",) # you need a comma if your tuple has just one item

hello_tuple = "hello",

# python can iterate through a tuple faster than a list


# getting things out of a tuple

colors = ('red', 'green', 'blue')

green = colors[1] # reference indexes just like you do in a list

blue_idx = colors.index("blue") # will return the index of the first match for blue


for idx, color in enumerate(colors): # use the enumerate with tuples
    print( idx, color)


# unpacking a Tuple

# pulling values out of a tuple setting them equal to a var to be manipulated

colors = ('red', 'green', 'blue')

red, green, blue = colors


# Sequences - lists, tuples, string - ordered, have indexes

# Slice [m:n] # slices up to but not including the number on the right 

name = "Alexandria"[0:4]

print(name)


colors = ('red', 'green', 'blue')[:2] # the slice makes a copy starting at the beginning

print(colors)


nums = [1,2,3,4,5,6,7,8,9,10][1:] # omitting the sequence up to the number given all the way to the end

print(nums)


fruit = ('apples', 'bananas', 'oranges')

fruit_copy = fruit[:]

print(fruit_copy)
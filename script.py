#excercise 1:
#Create a list named studentscontaining some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

studentscontaining = ["Tina", "Jenny", "Sara", "Sally", "Sue"]
print(studentscontaining[1])
print(studentscontaining[-1])

#excercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foodscontaining = ("pizza", "pasta", "salad", "chicken", "steak")
for food in foodscontaining:
    print(f"{food} goes here is a good {food}")

#excercise 3:
# Using a forloop, print just the last two food strings from foodscontaining.

for food in foodscontaining[-2:]:
    print(food)

#excercise 4:
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    "city": "San Francisco",
    "state": "California",
    "population": 1000000
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

#excercise 5:
#Iterate over the key: value pairs in home_townand print a string for each item, for example

for key, value in home_town.items():
    print(f"The {key} of my honetown is {value}")


#excercise 6:
#Create an empty list named cohort.
#Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape


cohort = []
student_names = ["Tina", "Jenny", "Sara", "Sally", "Sue"]

for student in student_names:
    cohort.append({"student": student, "fav_food": "pizza"})
    print(f"{student}'s favorite food is pizza")



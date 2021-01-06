"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

# Notes:
# A dictionary is like a list, except more general. In  a list, the indices (the index positions) have to be numbers, but in a dict it can be almost any type.
#  A dictionary is made of a collection of key (which is like the index) and value pairs, each key has a single value, and each pair is called a key-value pair or an item
#  Each key "maps" to a value
# You can create an empty dictionary with a set of curly brackets {} or with the built in function dict()
# Like this:
# new_dict = {}
# new_dict = dict()

# Also, note: do not use the word "dict" as a variable name because it is the name of a built in function. 
# Cool and maybe a little scary thing about Python, it is really easy to overwrite built in function, like the print() function, which is neat but also can really mess up your code, especially when you aren't sure what you overwrote.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({
    "lat": 57,
    "lon": -120,
    "name": "i don't know"
})
print(waypoints)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
# waypoints[0] = {
#     "lat": 43,
#     "lon": -130,
#     "name": "not a real place"
# }
waypoints[0].update(name = "not a real place", lon = -130)
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for fieldvalues in waypoints:
    print(fieldvalues["lat"], fieldvalues["lon"])
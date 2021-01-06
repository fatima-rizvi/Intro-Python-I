# Notes on classes:
#  PEP 8 recommendss using CamelCase to name classes

# Skip: Python uses Object Oriented Programming, which is a way of writing computer programs that use "objects" to model data ad behaviors. 
# The "objects" "talk" to one another to change the data within them.

# Further reading:
# dunder __repr__ method and dunder __str__ method (aka dunder methods, magic methods, protocols)
# https://docs.python.org/3/tutorial/classes.html
# Use dir() in the termnal to learn more about methods
# Type "python" to get into the python console
# then type something like "dir(str)" or whatever dir(`name of method`) you're interested in to get more documentation about it
# More reading on built in functions: https://docs.python.org/3/library/functions.html

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    # __init__ is an initializer , which is a special method that initializes an object. Al
    def __init__(self, lat, lon = None): # We pass self into the init method, which is a required argument in object methods. Self is simply a refrence to the object that the method is being invoked on
        self.lat = lat  # When we do this, we store the values of these onjects in attributes on the objects itself
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):     # Child of LatLon and parent of Geocache
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)  # Add .__init__(lat, lon) if you want to change lat and lon (kinda like @Override in Java? I think) BUT its best practice
    
    def __str__(self):  # Like init, str is another method that os supposed to return the string representation of an object. Goal is to make the object human readable. This is invoked by the print statement
        return f"{self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE        # Child of Waypoint and granchildof LatLon
class Geocache(Waypoint):
    def __init__(self, name, lat, lon, size, difficulty):
        self.size = size
        self.difficulty = difficulty
        super().__init__(name, lat, lon)
    
    def __str__(self):
        # return f"""
        # {self.name},
        # diff {self.difficulty},
        # size {self.size},
        # {self.lat},
        # {self.lon}
        # """
        # triple quotes = docstring
        return f"{self.name} is a geocache name"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)  # Creating a new instance of the Waypoint class

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint) #If you print an object it gives the memory location. That's why we did the str method

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 44.052137, -121.41556, 2, 1.5)     # Creating a new instance of the Gerocache class

# Print it--also make this print more nicely
print(geocache)

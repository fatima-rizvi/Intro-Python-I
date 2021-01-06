"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# Best oractice is to use a context manager, so with the with keyword
text = open("foo.txt", "r") 
print(text.read())
text.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

#a+ open and start a new file or add to one
# r+ opens a file for reading and writing
#w overwrite

# YOUR CODE HERE
bartext = open("baz.txt", "a+")
bartext.write("The cat in the hat\nknows a lot\nabout that")
bartext.close() #Close so it doesn't stay in memory

bartext = open("baz.txt", "w")
bartext.write("The cat in the hat\nknows a lot\nabout that")
bartext.close() #Close so it doesn't stay in memory

# use "a" to add to an existing file
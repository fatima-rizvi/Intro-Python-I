from dis import dis # Debugging
# Notes:
# First line of the function is the header, the lines indented below are the body. PEP-8 convention is to indent by four spaces


# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    # [num 0:2]
    # if num %2 == 0:
    #     return True
    # return False
    return num %2 == 0

print(is_even(7))
print(is_even(8))


# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)
# print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_odd(num):
    if num %2 == 0:
        print("Even!")
        return
    print("Odd!")

even_odd(9)
even_odd(8)

# dis(even_odd) # Debugging
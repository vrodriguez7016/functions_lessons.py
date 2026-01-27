# function = A block of reusable code
# place () after the function nhame to invoke it 

def happy_birthday(name, age): # name = parameter, temporary variable
    print(f"Happy birthday to {name}!") # procedure
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Bro", 20) # "bro" = argument, input for parameter
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)
# every argument needs corresponding parameter, order of arguments and parameters must match

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("BroCode", 42.50, "01/01")

# return = statement used to end a function
# and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# still have to invoke function to activate
# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)













# Methods, Help & Documentation Practice #1
# Remove the characters to the left of our main text:

# ,

# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.


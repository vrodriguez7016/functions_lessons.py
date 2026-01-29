def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, "ordered a ", tea_type, "tea")
    for arg in args:
        print("   - Add", arg)
    for key, value in kwargs.items():
        print("   - Add", key, ":", value)

tea_order("Alice", "chamomile") # Alice ordered a chamomile tea
tea_order("Bob", "black", milk="oat") # Bob ordered a black tea; add: oat
tea_order("Tony", "Black", "oat", sweetener="honey") # Tony ordered a black tea; add: oat, add: honey

eves_extras = {"milk": "almond", "sweetener": "sugar", "flavor": "lemon"}
tea_order("eve", "green", **eves_extras)
# *args allows for an indefinite amount of arguments since it continously creates new parameters
# **kwargs allows for keyboard arguments, acts as empty dictionary



# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    total = 0 # Initialize total to 0
    for num in args: # Iterate through each argument
        total += num ** 2 # Add the square of the number to total
        # first time through loop: total = 0 + 1^2 = 1
        # second time through loop: total = 1 + 1^2 = 5

    return total # return the total sum of squares
print(sum_squares(1, 2, 3)) # Example usage
print(sum_squares(4, 5, 6, 7, 8, 9)) # Example usage

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

def absolute_sum(*args):
    total = 0
    for num in args:
        total += abs(num)
    return total
print(absolute_sum(-1, 2, -3))
print(absolute_sum(-10, 20, -30, 40, -50))


# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum = 0
    for num in args:
        sum += num
    print(f"{name}, the sum of your numbers is {sum}")
personal_numbers("Vanessa", "18", "4", "9")

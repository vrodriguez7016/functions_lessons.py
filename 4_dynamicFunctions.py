# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

num = [7, 2, 5, -8, -14]
def all_positives(num):
    for i in range(len(num)):
        if num[i] <=0:
            return False
        else:
            return True
        
print(all_positives(num))

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.


def sum_less(nums):
    for i in range(len(nums)):
        if nums[i] > 0 and nums[i] < 1000:
            sum += nums[i]
        else:
            continue
    return sum





# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

def count_even(numbers):
    return sum(1 for x in numbers if x % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6]
count_even(numbers)

# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

#First Solution

# each string must index into the 10 numbers
# needs to be 3 seperate parts 
# each section should be joined by .join()
# return function should return all of the together, parentheses and space !

def create_phone_number(numbers):
    parentheses = ''.join(str(numbers[0]) + str(numbers[1]) + str(numbers[2]))
    middle = ''.join(str(numbers[3]) + str(numbers[4]) + str(numbers[5]))
    last = ''.join(str(numbers[6]) + str(numbers[7]) + str(numbers[8]))
    return '(' + parentheses + ')' + ' ' + middle + '-' + last

my_phone = create_phone_number([7, 1, 9, 5, 0, 5, 3, 7, 6, 2])
print(my_phone)

# Second Solution
# this is a more simlified, cleaner solution

# def create_phone_number(numbers):
#     formatted_number = f"({numbers[0:3]}) {numbers[3:6]}-{numbers[6:1]}"


# Third Solution (using Map function)

def create_phone_number_map(n):
    n = ''.join(map(str, n))
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"

print(create_phone_number_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
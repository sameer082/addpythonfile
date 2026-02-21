"""
creating a list from 0-10
and extracts the first five element
then reverse the elements
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = numbers[0:5]

reversed_list = first_five[::-1]# as we know empty spaces are default values

print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)
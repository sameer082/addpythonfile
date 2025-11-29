"""
Showing the number given
by the user is an even or odd
"""

number = int(input("Enter a number:"))

if number % 2 ==0:
    result = "Even"
else:
    result = "Odd"
print(f"{number} is an {result}")

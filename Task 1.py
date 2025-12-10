# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# Ask user for a number
num = int(input("Enter a number:"))

# Calculate and print  factorial
print(f"Factorial of {num} is {factorial(num)}")
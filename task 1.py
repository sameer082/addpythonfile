filename= "simple.txt"

try:
    file = open(filename , "r")
    print("This is the simple file for assignment 4")

    line_number  = 1
    for line in file:
        print("Line" , line_number , ":" , line, end="")
        line_number +=1
    file.close()

except FileNotFoundError:
    print(f"Error: The file {filename} was not found")
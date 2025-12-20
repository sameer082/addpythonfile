# Here we get the problem to make a file and over writing the file

text = input("Enter text to write to the file:")

file =open("output.txt" ,"w")
file.write(text + "\n")
file.close()

print("Data successfully written to output.txt")

more_text = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(more_text + "\n")
file.close()

print("Data successfully appended.")

file = open("output.txt" ,"r")
content = file.read()
file.close()
print("\nFinal content of output.txt:")
print(content)
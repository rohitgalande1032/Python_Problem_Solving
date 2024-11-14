# Files are used to data permanently in memory
# Operations on file
# 1. Open File
# 2. Read/Write 
# 3. Close the file

file = open("file.txt", "r")  # Open for reading
content = file.read()  # Reads the entire file
print(content)
file.close()  # Close the file

file = open("example.txt", "w")
file.write("Hello, World!\n")  # Write a line of text
file.write("Writing another line.\n")
file.close()

file = open("example.txt", "a")
file.write("Appending new line.\n")
file.close()


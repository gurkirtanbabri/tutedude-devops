filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()
print("File content:")
print(content)
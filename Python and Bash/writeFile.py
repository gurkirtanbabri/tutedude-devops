filename = input("Enter the filename to write to: ")
content = input("Enter the content to write into the file: ")

with open(filename, 'w') as file:
    file.write(content)
print(f"Content written to {filename}")

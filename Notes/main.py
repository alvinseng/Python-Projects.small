# Open and read

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# file.close()

#open and write

with open("my_file.txt", mode="a") as file:
    file.write("\nNew_text")
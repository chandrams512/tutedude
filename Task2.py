# Task 2
# Step 1: Take user input and write to the file (overwrite mode)
user_text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_text + "\n")

# Step 2: Take more input and append to the file
user_text2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(user_text2 + "\n")

# Step 3: Read and display final content
with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal file content:\n")
    print(content)

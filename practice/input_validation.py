age = input("Enter your age: ")

while not age.isdigit():
    age = input("Invalid input. Enter a number: ")

print("Your age is", age)
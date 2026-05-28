print("This is a simple calculator")
print("What function would you like to apply?")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

function = int(input())

if function == 1:
    a = input("What's the first number?")
    b = input("What's the second number?")
    print(int(a) + int(b))

elif function == 2:
    a = input("What's the first number?")
    b = input("What's the second number?")
    print(int(a) - int(b))

elif function == 3:
    a = input("What's the first number?")
    b = input("What's the second number?")
    print(int(a) * int(b))

elif function == 4:
    a = input("What's the first number?")
    b = input("What's the second number?")
    print(int(a) / int(b))

else:
    print("You have entered an invalid function. Please run the program again.")
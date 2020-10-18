import sys                          # needed for exit program with error code

try:
    x = int(input("x: "))           # 5
    y = int(input("y: "))           # 0 will run into exeption
except ValueError:                  # if input is a word like "hello"
    print("Invalid Input.")         # exeption "ValueError" is showing up. therefore using try for inputs here.
    sys.exit(1)

try:                                # handling the exeption
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot devide by 0.")
    sys.exit(1)                     # exit with error code 1

print(f"{x} / {y} = {result}")

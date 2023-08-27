import sys


user = (input("Enter a number: "))

if user == "quit":
    sys.exit()
elif (int(user) < 5 or int(user) > 9):
    raise ValueError("not in between 5 and 9")

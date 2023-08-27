# EXECUTE THE LOOP BODY FIRST AND THEN CHECK THE CONDITION

while True:
    user = int(input("Enter a number:"))
    print(user)
    if not user > 0:
        break

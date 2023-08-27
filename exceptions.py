try:
    num = int(input("Enter a number:"))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

except Exception:
    print("Sorry some error occurred")

# COUNT NUMBERS IN A STRING
# 1.
s = input("Enter: ")
count = 0
for i in s:
    if i.isnumeric():
        count += 1
print(f"Digits: {count}")

# 2.
s = input("Enter: ")
numbers = '1234567890'
count = 0
for i in s:
    if i in numbers:
        count += 1
print(f"Digits: {count}")

# PARTICULAR CHARACTER COUNT
# 1
s = input("Enter: ")
letter = input("Letter: ")
count = 0
for i in s:
    if i == letter:
        count += 1
print(f"{letter} is repeated : {count}")

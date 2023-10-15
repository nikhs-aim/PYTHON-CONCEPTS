# REVERSE
# 1.
s = input("Enter: ")
print(s[::-1])

# 2- for numbers
s = int(input("Enter: "))
rev = ''
num = ''
while s != 0:
    num = s % 10
    rev += str(num)
    s = s//10
print(rev)

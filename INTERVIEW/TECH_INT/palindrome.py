# PALINDROME
# 1.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# 2.
s = input("Enter a string: ")
for i in range(0, int(len(s)/2)):
    if s[i] == s[len(s)-i-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


# 3.
st = input('')
j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("NO")
else:
    print("Yes")

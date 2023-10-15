'''You have write a function that accepts, a string which length is “len”, the string has some “#”, in it you have to move all the hashes to the front of the string and return the whole string back and print it.'''
a = input("Enter: ")
hash = ""
for i in a:
    if i == "#":
        hash += i
        a = a.replace("#", "")

print(hash+a)


'''You have two numbers number1 and number2, your job is to check the number of borrow operations needed for subtraction of number1 from number2. If the subtraction is not possible then return the string not possible.'''
a = int(input("1:"))
b = int(input("2:"))
count = 0

if a < b:
    print("Not possible")
else:
    flag = 0  # at start there will be no borrow operations
    while a != 0 and b != 0:  # if it is zero then it terminates
        temp1 = 0
        temp2 = b % 10  # store the last digits of second number

        if flag:  # here if flag means flag=1, borrow operation ws performed in previous operation
            temp1 = a % 10-1  # previous no borrow operations means
        else:
            temp1 = a % 10

        if temp1 < temp2:
            count += 1
            flag = 1
        else:
            flag = 0

        a = a//10
        b = b//10
print(count)


'''You’re given a function that accepts the following, a string1, its length and a character c. Your job is to replace all the occurrences of character c in string1 and capitalize it or decapitalize it based on the character c.'''
user = input("Enter:")
letter = input("Letter: ")
ans = ''
for i in range(len(user)):
    if user[i] == letter:
        # print(user[i])
        ans += user[i].upper()
    else:
        ans += user[i]
print(ans)


'''You’re given a string where multiple characters are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :

Input :
aabbbbeeeeffggg

Output:
a2b4e4f2g3'''

user = input('Enter: ')
ans = ''
for i in range(len(user)):
    if not user[i] == user[i-1]:
        if user.count(user[i]) <= 1:
            ans += user[i]
        else:
            ans += user[i]
            ans += str(user.count(user[i]))


print(ans)


'''You’re given a string, you’ve to print additional characters needed to make that string a palindrome.'''


def ispalindrome(s):
    return s == s[::-1]


def solve(s):
    if ispalindrome(s):
        return None
    for i in range(len(s)):
        x = s[:i][::-1]
        if ispalindrome(s + x):
            return x


s = input()
# print(solve(s))

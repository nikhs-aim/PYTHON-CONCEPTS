# ENCODE

import random
user = input("Enter the string to encode:")

if len(user) >= 3:
    store = user[0]
    # print(store)
    rem = user[1:len(user)]
    # print(rem)
    app = (rem+store)
    # print(app)
    letters = "abcdefghijklmnopqrstuvwxyz"
    beg_random_letters = "".join(random.choices(letters, k=3))
    # print(beg_random_letters)
    beg = beg_random_letters + app
    # print(beg)
    end_random_letters = "".join(random.choices(letters, k=3))
    # print(end_random_letters)
    complete = beg_random_letters+app+end_random_letters
    print(complete)
else:
    print(user[-1::-1])


# DECODE

user = input("Enter the string to decode: ")

beg = user[3:]
# print(beg)

end = beg[-3::1]
# print(end)

actual = beg.replace(end, " ")
# print(actual)

rep = actual[-2]
# print(rep)

print(rep+actual[0:len(actual)-2])

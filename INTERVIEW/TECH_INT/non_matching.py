# TO FIND NON MATCHING CHARACTERS IN A STRING
# 1
s = input("Enter: ")
nm = ''
for i in s:
    if s.count(i) == 1:
        nm += i
print(f"The non matching characters are '{nm}'")


# 2
a = input("1: ")
b = input("2: ")
nm = ''
for i in a:
    if i not in b:
        nm += i
for i in b:
    if i not in a:
        nm += i


nm_set = sorted(set(nm))
for i in nm_set:
    print(i, end=" ")


# 3
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


a = input("1: ")
b = input("2: ")
nm = ''
for i in a:
    if i not in b:
        nm += i
for i in b:
    if i not in a:
        nm += i
nm_set = list(set(nm))
sorted_nm_set = bubble_sort(nm_set)
for i in sorted_nm_set:
    print(i, end=" ")

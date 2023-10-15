# TO CALCULATE NUMBER OF VOWELS AND CONSONANTS
s = input("Enter: ")
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
vow_count = 0
con_count = 0

for i in s:
    if i.lower() in vowels:
        vow_count += 1
    elif i.lower() in consonants:
        con_count += 1

print(f"Number of vowels: {vow_count}")
print(f"Number of consonants: {con_count}")

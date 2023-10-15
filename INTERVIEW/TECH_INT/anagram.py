# TO FIND OUT WHETHER THE TWO STRINGS ARE ANAGRAMS

a = input("1: ")
b = input("2: ")

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")

'''
NAVHW_058: Write a program to count the number of vowels and consonants in a string entered by the user.

Input:
Abcde

Output:
Vowels - 2
Consonants - 3

Input:
Chef IS coOking

Output:
Vowels - 5
Consonants - 8

Input:
Aaaa

Output:
Vowels - 4
Consonants - 0
'''
list_of_vowels = ["a","e","i","o","u"]
vowels = 0
space = 0
name = input("Enter to count vowels & consonants:-  ")
for i in name:
    if i == " ":
        print("space ",i)
        space+=1
    for j in list_of_vowels:
        if i.lower()==j:
            vowels+=1
print(vowels," vowels")
consonants = len(name)-(vowels+space)
print(consonants," consonants")
        

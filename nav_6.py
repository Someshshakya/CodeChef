'''
Write a program to take a number as input from the user and print
“Bingo” - If the number is even and >200
“Ringo” - If the number is odd and <200
“CodeChef” - for any other number 
Note: You cannot use and/or operator
'''
n = int(input("Enter your number :   - "))
if n%2==0:
    if n>200:
        print("Bingo")
    else:
        print("codeChef")
else:
    if n < 200:
        print("Ringo")
    else:
        print("CodeChef")
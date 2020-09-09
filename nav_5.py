# Write a program to take two numbers A and B as input 
#from the user and print the number less than A which completely divides the number.
"""
For example:
A = 23, B = 7
For 23 % 7:: 21 is the number which is completely divisible by B i.e, 7.

A = 13, B = 5
For 13 % 5:: 10 is the number which is completely divisible by B i.e, 5.
"""
a = int(input("Enter Your number  :- "))
b = int(input("Enter Your number  :- "))
if a%b!=0:
    tem = a%b
    print(a-tem,"is the number which is completely divisible by B i.e,  ",b)
else:
    print(a,"is the number which is completely divisible by B i.e,  ",b)
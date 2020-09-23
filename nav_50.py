'''
NAVHW_050: Draw a flowchart to take N as input and print the following sequence.

Sample Input
9

Sample Output
10 2 20 4 30 6 40 8 50
'''
n = int(input("enter n number to print the pattern:  "))
odd = 10
even = 2
for i in range(1,n+1):
    if i%2!=0:
        print(odd,end=" ")
        odd+=10
    else:
        print(even,end=" ")
        even+=2
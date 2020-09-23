'''NAVHW_051: Draw a flowchart to take N as input and print the following sequence till N.
Sample Input 
9
Sample Output 
1 13 7 10 26 8 100 39 9
'''
n = int(input("Enter n number to print the pattern :   "))
a = 1
b = 13
c = 7
for i in range(1,n+1):
    if (i%3==0):
        print(c,end=" ")
        c+=1
    elif (i%3==1):
        print(a,end=" ")
        a *= 10
    elif (i%3==2):
        print(b,end=" ")
        b+=13
   
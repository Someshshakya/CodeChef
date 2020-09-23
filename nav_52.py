'''
NAVHW_052: Draw a flowchart to take N as input and print the following pattern.
Sample input
4
Sample output
    *
   ***
  *****
 *******
'''

# Each time the star pattern is increasing by i+2
count = 1
n = int(input("Enter your number"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*count)
    count+=2
    



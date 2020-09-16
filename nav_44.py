'''NAVHW_044: Draw a flowchart to take N as input and print numbers from 1 to N, 5 times.
Sample Input 
6
Sample Output
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
'''
num = int(input("Enter your number for the pattern:  "))
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end=" ")
    print()
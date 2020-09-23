'''NAVHW_059: Draw a flowchart to take an input N and print the following sequence.
Sample Input
5
Sample Output
5 4 3 2 1
10 9 8 7 6
15 14 13 12 11
20 19 18 17 16
25 24 23 22 21
'''
n = int(input("Enter the nuber :   "))
k = n
for d in range(n):
    c = k
    for j in range(n):
        print(c,end=" ")
        c-=1
    k+=5
    print()

'''NAVHW_048: Draw a flowchart to print following sequence

1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''
n = int(input("Enter your number   "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
        if j==i:
            for k in range(j-1,0,-1):
                print(k,end=" ")
    print()
    
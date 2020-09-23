'''
NAVHW_053: Draw a flowchart to take an input N and print the following sequence.
Sample input
5
Sample Output
1
2 3 2
3 4 5 4 3
4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''




n  = int(input("Enter your number to form the pattern-:  "))
count = 1
d = 1
while count<= n:
    # to print the pattern in increasing order
    m = count
    while m<d:
        print(m,end=" ")
        m+=1
    # to print the pattern in reverse order after reaching the n number

    while m>=count:
        print(m,end=" ")
        m-=1
    print()
    count +=1
    d += 2
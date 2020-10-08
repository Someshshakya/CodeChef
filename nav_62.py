'''NAVHW_062: Write a code to take N & M as input followed by items of each list. 
The lists provided are already sorted in non-decreasing order. You need to merge both lists 
and produce a merged sorted list. (Without using sort function / any other sorting technique) HINT: Lists are already sorted.

Sample Input 
5 
1 2 3 4 55
4
43 44 56 7643 44 56 76

Sample Output
1 2 3 4 43 44 55 56 76
'''
n1 = int(input("Enter number limit:-  "))
n = [int(k) for k in input("Enter your number:  ").split()]
m1 = int(input("Enter number limit:--  "))
m = [int(k) for k in input("Enter your number:  ").split()]
if (len(n)==n1 and len(m)==m1):
    if n[0] > m[0]:
        new_list = m+n
        print(new_list,"hi")
        for j in (new_list):
            print(j,end=" ")
    else:
        new_list = n+m
        print(new_list)
        for i in (new_list):
            print(i,end=" ")
else:
    print('Enter limited numbers only!')


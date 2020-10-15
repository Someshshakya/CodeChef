'''NAVHW_062: Write a code to take N & M as input followed by items of each list. 
The lists provided are already sorted in non-decreasing order. You need to merge both lists 
and produce a merged sorted list. (Without using sort function / any other sorting technique) HINT: Lists are already sorted.

Sample Input 
5 
1 2 3 4 55
4
43 44 56 76

Sample Output
1 2 3 4 43 44 55 56 76
'''
a = int(input("Enter number limit:-  "))
n = [int(k) for k in input("Enter your number:  ").split()]
b = int(input("Enter number limit:--  "))
x = [int(k) for k in input("Enter your number:  ").split()]
merged_list = []
if len(n)==a and len(x)==b:
    while True:
        if len(n)==0:
            merged_list = merged_list + x
            break
        elif len(x)==0:
            merged_list = merged_list+n
            break
        else:
            if n[0] < x[0]:
                merged_list.append(n[0])
                n.pop(0)
            else:
                merged_list.append(x[0])
                x.pop(0)
    print(merged_list)
else: 
    print("Plz put the element within range only!")
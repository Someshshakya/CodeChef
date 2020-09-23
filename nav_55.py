'''NAVHW_055: Draw a flowchart to take N as input, followed by N elements. Take another input X and check whether it exists in the given N elements.
Sample Input:
7
1
3
4
5
34
87
990
6 (X)
Sample Output
NO
'''
# to take n elements in the list 
my_list = []
n = int(input("To take n elements in the list:---    "))
for i in range(n):
    my_list.append(input("Enter your elements :    "))
check = input("Enter the x elements to check: in the list:--   ")

# to check the elements in the list 
for elements in my_list:
    if elements==check:
        print("yes")
        break
else:
    print("no")

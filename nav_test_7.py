'''NAVTEST_7: Draw a flowchart to Take 10 numbers as input and create a 
list of the numbers from the user and update each element of the list according to below rule
If it is even, then multiply it by 100
If it is odd, then multiply it by -1
	
Input:
23
42 
41 
1
	
Output:
-23 
4200 
-41 
-1
'''

# to take 10 numbers input 
n = 10
my_list = []
for j in range(n):
    num = int(input("enter number to update:-  "))
    if num%2==0:
        num*=100
        my_list.append(num)
    else:
        my_list.append(num*(-1))
for i in my_list:
    print(i)
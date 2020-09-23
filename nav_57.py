'''NAVHW_057: Draw a flowchart to create a list of 7 numbers from the user,
 print true if the complete list consists of consecutive numbers or not.
Input:
1 2 3 4 5 6 7
Output:
True

Input:
45 46 47 48 49 51 52
Output:
False

Input:
4 5 6 7 8 9 10
Output:
True

Input:
-5 -6 -7 -8
Output:
False

Input:
-3 -2 -1 0 1
Output:
True
'''
n = 7
list_to = []
for i in range(n):
    list_to.append(input("enter n consecutive numbers:---   "))
num = int(list_to[0])
for j in (list_to):
    if int(j)!=num:
        print(False)
        break
    num+=1
else:
    print(True)
        
    

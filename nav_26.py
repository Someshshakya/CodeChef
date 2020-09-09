''' Draw a flow chart to print numbers from N to 1, where N is given as an input from the user.
Sample Input:
5
Sample Output:
		5
		4
		3
		2
		1
'''
n = int(input("Enter your number to print nubers to 1:-   "))
for i in range(n,0,-1):
    print(i)
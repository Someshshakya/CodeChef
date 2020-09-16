'''
NAVHW_032:: Draw a flowchart to input a number, print all of its factors.
Sample Input:
5
Sample Output:
1
5

Sample Input:
6
Sample Output
1
2
3
6
'''
n = int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
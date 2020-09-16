'''NAVHW_043: Draw a flowchart to check if the number entered by the user is palindrome
Sample Input
121
Sample Output 
YES
Sample Input
1212
Sample Output
NO
'''
num = int(input('Enter any number:   '))
palindrome = num
check = 0
while num !=0 :
    mod = num%10
    check = (check*10)+mod
    num //= 10
    
if check == palindrome:
    print("Yes")
else:
    print("NO")
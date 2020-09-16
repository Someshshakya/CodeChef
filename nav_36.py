'''NAVHW_036: Draw a flowchart to input a number and print the reverse of that number
	Sample Input:
	104
Sample Output:
	401

Sample Input:
	212
Sample Output:
	212
'''
number = int(input('Enter the number:  '))
reverse = 0
while number != 0:
    mod = number % 10
    print(mod)
    reverse = (reverse * 10) + mod 
    number //= 10
print(reverse)
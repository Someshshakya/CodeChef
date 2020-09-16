'''NAVHW_040: Draw a flowchart to print fibonacci of a given number.
		https://en.wikipedia.org/wiki/Fibonacci
	Sample Input
		4
	Sample Output
		3
'''
num = int(input("Enter your number:  "))
initial = 0
nextt = 1
c = 1
while c<=num:
    new = initial
    initial = nextt
    nextt = new + initial
    c+=1
    
print(initial)
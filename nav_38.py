'''
NAVHW_038: Draw a flowchart to input a number and check whether 
the entered number is a perfect number or not. (A perfect number - the sum of the factors less than n is equal to the number 
Example- 6 - 1+2+3 = 6)
	Sample Input:
	6
	Sample Output:
	Perfect number

	Sample Input:
	5
	Sample Output:
	Not a perfect number'''
n = int(input("Enter the number :  "))
check = n 
sum = 1
c = 2
while c*c <=n:
    if n%c==0:
        sum += c
        if n//c!=c:
            sum += (n//c)
    c+=1
print()
if sum == check:
    print(" perfect number")
else:
    print("no")
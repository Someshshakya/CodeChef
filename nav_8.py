'''Write a program that takes a number n and checks if the number is an odd multiple of 3.
	Example
		n = 24
			Not odd multiple of 3.
		n = 21
			Odd multiple of 3
'''

n = int(input("Enter your number:   -  "))  
if n%3==0 and n%2!=0:
    print("This is the odd multiple of 3   ",n)
else:
    print("This is not the odd multiple of 3 ",n)
'''Draw a flow chart to print Hello “name” for 20 times, here “name” is entered by the user
Sample Input:
Jane Doe
Sample Output:
Hello Jane Doe
	..(18)
Hello Jane Doe
'''
input=input("Enter your name: ")
a = 1
while a <= 20:
      print(" Hello "+input)
      a +=1
'''NAVHW_025:: Draw a flow chart to print the sum of numbers from 1 to N, where N is given as an input from the user
Sample input
5  
Sample output
15'''
input = int(input("Enter your number: "))
a = 1
sum  = 0
while a <= input:
      sum += a
      a += 1
print("Total_Sum = ",sum)
'''NAVHW_031:: Draw a flowchart to input a number and check if its second last digit is 7 or not.
Sample Input:
276
Sample output:
Yes
'''
n = int(input("enter a number "))
mod = (n%100)//10 # Here you will get the last digit
if mod == 7:
    print("yes 7 is the 2nd last digit of a number ",mod)
else:
        print("no 7 is not  the 2nd last digit of a number  ",mod)


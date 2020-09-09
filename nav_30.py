'''NAVHW_030:: Draw a flow chart to take input and check if the number ends with 7 or not.
 If it does, print “Yes” else “No” → eg. 7, 77, 87, 967.'''
n = int(input("Enter your number:-    "))
mod = n%10
if mod==7:
    print('yes')
else:
    print("no")
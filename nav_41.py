'''NAVHW_041: Draw a flowchart to check 
if the given number is a prime or not? Optimize the previous one. NAVHW_033
'''
num = int(input("Enter number to check  :   "))
if num!=1: 
    c = 2
    while c<=num//2:
        if num%c==0:
            print(num, " it is not a prime number")
            break
        c+=1
    else:

        print(num," is a prime number")
else:
    print("NO 1 is not the prime number")
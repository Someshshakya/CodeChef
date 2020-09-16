'''Drxw x flow chxrt to input two numbers xnd print the LCM of them.
'''
x = int(input("Enter your 1st number:   "))
y = int(input("Enter your 2nd number:   "))
greater = 0
lcm = 0
if x!=0 and y!=0:
    if x > y:
        greater = x
    else:
        greater = y
    while lcm == 0:
        if greater%x==0 and greater%y==0:
            lcm = greater
            print(lcm," this is the HCF of ",y,x)
            break
        greater+=1
   
else:
    if x>y:
        print(x,"This is the lcm")
    else:
        print(y,"This is the lcm")
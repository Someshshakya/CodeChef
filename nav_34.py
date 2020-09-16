'''NAVHW_034:: Try to optimize/reduce the number of iterations of loop in the NAVHW_032.'''
n = int(input("Enter your number to find it's factors:  "))
c = 1
while c*c <=n:
    if n%c==0:
        print(c)
        if n//c!=c:
            print(n//c) 
    c+=1
'''Write the program to check NAVHW_014 then print NAVHW_015.
'''
a = int(input("Enter the angle of the Triangle:  "))
b = int(input("Enter the angle of the Triangle:  "))
c = int(input("Enter the angle of the Triangle:  "))

if a!=0 and b!=0 and c!=0:
    if (a+b+c == 180): 
        if (a == 90 or b==90 or c==90):
            print('This is angle is right angled Triangle')
        elif (a < 90 and b<90 and c<90):
            print("This is an Acute angled Triangle")
        else:
            print("This is an Obtuse angled Triangle")
    else:
        print("NO it is not possible to form !")
else:
    print("The tringle is not able is form ! ")
'''Write a program to input three angles of a triangle and check 
which type of triangle based on the angles - right, obtuse, acute.'''

a = int(input("Enter the angle of the Triangle:  "))
b = int(input("Enter the angle of the Triangle:  "))
c = int(input("Enter the angle of the Triangle:  "))

if (a == 90 or b==90 or c==90):
    print('This is angle is right angled Triangle')
else:
    if (a < 90 and b<90 and c<90):
        print("This is an Acute angled Triangle")
    else:
        print("This is an Obtuse angled Triangle")

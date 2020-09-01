''': Write a program to input three angles of a triangle and check if that 
triangle is possible to form? [hint: Sum of all the angles must be equal to 180 degrees]'''

a = int(input("Enter the angle of the Triangle:  "))
b = int(input("Enter the angle of the Triangle:  "))
c = int(input("Enter the angle of the Triangle:  "))

if a!=0 and b!=0 and c!=0:
    if (a+b+c == 180):
        print("The triangle is possible to from ")
    else:
        print("NO it is not possible to form !")
else:
    print("The tringle is not able is form ! ")


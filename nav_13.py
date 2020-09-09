'''Write a program to check NAVHW_010 and then NAVHW_012. 
First, check whether the triangle is valid or not. If valid, check whether it is equilateral, isosceles or scalene.
'''

if (a+b>c and a+c>b and b+c>a):
    if (a==b==c):
        print("The tringle is Equalateral Tringle ")
    else:
        if (a==b or b==c or a==c):
            print("This is an isoceles Tringle ")
    else:
        print("The Tringle is Scalene")
else:
    print('This triangle is not possible...')
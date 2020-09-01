''' Write a program to input three sides of a triangle 
and check if a triangle is equilateral, isosceles or scalene.'''

a = int(input("Enter the side of the triangle :-  "))
b = int(input("Enter the side of the triangle :-  "))
c = int(input("Enter the side of the triangle :-  "))

if (a+b>c and a+c>b and b+c>a):
    if (a==b==c):
        print("The tringle is Equalateral Tringle ")
    elif (a==b or b==c or a==c):
        print("This is an isoceles Tringle ")
    else:
        print("The Tringle is Scalene")
else:
    print('This triangle is not possible...')
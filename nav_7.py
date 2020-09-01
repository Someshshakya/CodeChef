'''Write a program to input three sides of a triangle and check if the triangle is valid. 
Sum of 2 sides should be greater than the third side which means 
a+b>c and a+c>b and side_3+b>a ⇒  Then triangle is possible.'''
a = int(input("Enter the side of a triangle:  "))
b = int(input("Enter the side of a triangle:  "))
c = int(input("Enter the side of a triangle:  "))

if (a + b > c) and (a +c > b) and (b + c > a):
    print("It is posible")
else:
    print("not posible")
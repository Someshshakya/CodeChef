# Write a programme for swapping two numbers without using 3rd/temp variable. (Without using a,b = b,a)
a = int(input(" Enter you 1st value a  - "))
b = int(input("Enter your n2 value  b  - "))
b = b+a
a = b-a
b = b-a

print("After swapping a ",a)
print("After swapping b ",b)
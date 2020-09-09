# Write a programme for finding the maximum of 3 number.
n1 = int(input("Enter your number "))
n2 = int(input("Enter your number "))
n3 = int(input("Enter your number "))
if n1<n2:
    if n2<n3:
        print(n3,"This is the max")
    else:
        print(n2,"this is the max")
else:
    if n1>n3:
        print(n1,"this is the max")
    else:
        print(n3,"this is the max")
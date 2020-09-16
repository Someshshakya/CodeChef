'''Draw a flow chart to input two numbers and print the HCF of them.'''
num_1 = int(input("Enter your 1st number:   "))
num_2 = int(input("Enter your 2nd number:   "))
smaller = 0
if num_1 < num_2:
    smaller = num_2
else:
    smaller = num_2

while smaller >= 1:
    if num_1%smaller==0 and num_2%smaller==0:
        print(smaller," this is the HCF of ",num_2,num_1)
        break
    smaller-=1


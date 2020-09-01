# Write a code for finding the 2nd maximum number from 3 numbers given as input. (Without using AND / OR)

num_1 = int(input("Enter your number  "))
num_2 = int(input("Enter your number  "))
num_3 = int(input("Enter your number  "))

if num_1 < num_2:
    if num_2 < num_3:
        print(num_2,"this is the 2nd max ")
    else:
        print(num_3,"this is the 2nd max")
else:
    if num_1 > num_3:
        if num_2 < num_3:
            print(num_3,'this is the 2nd max')
        else:
            print(num_2,"this is the 2nd max")
    else:
        print(num_1,'this is the 2nd max')

        
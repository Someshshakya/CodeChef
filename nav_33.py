'''NAVHW_033:: Write a program to input a number and check if the number is prime or not.
Sample Input:
4

Sample Output:
Not a prime number

Sample Input:
11

Sample Output:
Prime number'''

check = int(input("Enter number to check  :   "))
if check!=1: # checking for 1 
    div = check-1
    while div >=2:
        if check%div==0:

            print(check, " it is not a prime number")
            break
        div-=1
    else:
        print(check," is a prime number")
else:
    print("NO 1 is not the prime number")
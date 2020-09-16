'''NAVHW_042: Draw a flow chart to take an input N and print first N prime numbers.
Sample Input:
5
Sample Output
2
3
5
7
11
'''
number = int(input("Enter your number to print prime number till nth no.  "))
j = 1 # this will count the number of prime numbers
num = 2
while j <= number:
    c = 2
    while c<=num//2:
        if num%c==0:
            
            break
        c+=1
    else:
        print(num)
        j+=1
    num+=1  # if the number is prime it will check for next number
'''
 Draw a flowchart to check if the given number is a strong number or not.
A strong number is a special number whose sum of the factorial of digits is equal to the original number. 
For example, 145 is a strong number. Since, 1! + 4! + 5! = 145
'''
num = int(input('Enter the number:  '))
check = num # this will contain the value of the user 
sum = 0
while num != 0 :
    facto = num % 10
    mul = 1
    while facto > 0:
        mul *= facto
        facto -= 1
    sum+=mul
    num //=10
print(check,sum)
if check == sum:

    print("This is a strong number: ")
else:
    print("NO this is not a strong number: ")
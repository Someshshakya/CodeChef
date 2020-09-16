'''NAVHW_035:: Draw a flowchart to take a number N as input and print the sum of digits of that number.

SAMPLE INPUT
3425
SAMPLE OUTPUT
14

EXPLANATION: (3+4+2+5) = 14
'''
num = int(input('Enter the number: '))
sum = 0 
while num != 0:
    mod = num%10
    sum+=mod
    num//=10
print(sum)

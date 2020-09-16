'''NAVHW_039: An Armstrong number is an integer such that the sum of the cubes of its digits is equal to the number itself. 
For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371. 
Draw a flowchart to find all Armstrong numbers in the range of 0 and 999.

123
1**3 + 2**3 + 3**3 = 1 + 8 + 27 = 36

153
1**3 + 5**3 + 3**3 = 1+ 125 + 27 = 153
'''

num = int(input('Enter your number: '))
check = num 
sum = 0
while num != 0:
    mod =num%10
    sum += mod**3
    print(sum)
    num //= 10
if sum==check:
    print("This is an  armstrom number ",check)
else:
    print("Noo this is not an  armstrom number",check)
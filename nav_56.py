'''NAVHW_056: Given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ 
elements of the given list. ‘N’ is accepted from the user.
Input:
1

Output:
q 

Input:
3

Output:
5
b 
q

'''
my_list = ["a","c",3,"n","k",4]
n = int(input("Enter the number:-   "))
# to print the elements from the list till the last
for index in range(n,0,-1):
    print(my_list[index*(-1)])
'''NAVHW_046: Draw a flowchart to print the first 10 numbers of the following series -
1, 2, 4, 7, 11,...
1, 11, 31, 61, 101,...
1, 3, 7, 13, 21,...
'''
                    # pattern for >>>>    1, 2, 4, 7, 11,...

n  = int(input("Enter the number:   "))
start = 1
dif = 0
for i in range(n):
    start += dif
    print(start)
    dif += 1


                        # pattern for >>>>>>>>>>>>>> 1, 11, 31, 61, 101,...

# n  = int(input("Enter the number:   "))
# start = 1
# dif = 0
# for i in range(n):
#     start += dif
#     print(start)
#     dif += 10



                        # pattern for >>>>>>>>>>>>>> 1, 3, 7, 13, 21,...

# n  = int(input("Enter the number:   "))
# start = 1
# dif = 0
# for i in range(n):
#     start += dif
#     print(start)
#     dif += 2
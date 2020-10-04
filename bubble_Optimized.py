''' 
To optimize the time complexity what i did is i went through 
each iteration  of the list what was going on !
I found that when the list get sorted then, there is no swapping  taking place so 
I kept that in tracked and when it is not swapping it will terminate at that time only 
and we get the sorted list.
'''
#     without optimization
print("\t\t\t\t\t\t\twithout optimization")
arr = [2, 3, 32, 21, 43,4, 223]
c = 1
for i in range(len(arr)):
    for k in range(0,len(arr)-i-1):
        #to keep track on number of steps
        c+=1
        if arr[k] > arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print(arr,"  Total steps taken:-  >>>>>>>>>>>>>>>>>>>   ",c)



# After optimizing the code 
#  it will not take spare time
print("\t\t\t\t\t\t\tAfter optimizing")


arr = [2, 3, 32, 21, 43, 4, 223]
c = 1
for i in range(len(arr)):
    #
    swap = True
    for k in range(0,len(arr)-i-1):
        #to keep track on number of steps
        c+=1
        if arr[k] > arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
            #to track swapping
            swap = False
    # teminate if there is no swapping 
    if swap:
        break
print(arr,"  Total steps taken:-  >>>>>>>>>>>>>>>>>>>   ",c)
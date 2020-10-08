# NAVHW_061: Find the time Complexity of these
 
for i in range (2*N):
    print(i)

O(N) O of N
##


for i in range (2**N):
    print(i)
    
~O(2^N) O of 2 to the power of N

##
for i in range (N**(2*2)):
    counter += 1
    
# ~O(n^2) O of n to the power of 2
##
for i in range (N**(2**0.5)):
    counter += 5;

    # ~O(n^2) O of n to the power of 2

    
##
for i in range (N, N**2):
    print(i)
     # ~O(n^2-n) O of n to the power of 2 and N is subtracted
    
##
for i in range (1, N**3):
    counter += N
     # ~O(n^3) O of n to the power of 3
##
for i in range (N**(0.5), N, 2):
    print(i)
 # ~O(n) O of n
##
for i in range (N, 2*N, N):
    print(i)
     # ~O(1) O of 1
    
##
for i in range (N**2):
    for j in range (i):
        print (i*j)
         # ~O(n^2) O of n to the power of 2

##
for i in range (N):
    for j in range(2**N):
        for k in range (N**2):
            print(i*j+k)
         # ~O(2^n) O of 2 to the power of n
##
while N > 0: 
    N //=2
    print(N)
    # ~O(log n) 
    


##
while N > 0:
    N //= N
    print(N)
    # ~O(infinite) O of infinite

    
##
while N > 0:
    N -= 10
    print(N)
#~O(n/10) O of N divided by 10

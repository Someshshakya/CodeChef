'''NAVHW_049: Draw a flowchart to print the following sequence.
        *
      * *
    * * *
  * * * *
* * * * *

'''

n = int(input('Enter the start pattern number:   '))
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)
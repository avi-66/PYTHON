''' ASTRIC PYRAMID: 
n=3
  *
 ***
***** 
'''
n=int(input("Enter the Number of Lines :"))
m=n-1
for i in range (1,n+n,2):
     print (" "*m+"*"*i)
     m=m-1

#Sum of Digits
print('Enter a Number')
n=int(input())
r=0
s=0
while(n>0):
   r=n%10
   s=s+r
   n=n//10
print(s)

#Swap 2 variables without using 3rd variable
print('Enter a & b')
a=int(input())
b=int(input())
print('Before Swap','a='+str(a),'b='+str(b))
a,b=b,a
print('After Swap','a='+str(a),'b='+str(b))

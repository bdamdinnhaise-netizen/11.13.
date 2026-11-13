n=12345
a=0
b=0
while n>0:
    x=n%10
    if x%2==0:
        a=a+1
    else:
        b=b+1
    n=n//10
print(a)
print(b)
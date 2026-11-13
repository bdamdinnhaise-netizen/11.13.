n=5832
a=9
while n>0:
    x=n%10
    if x<a:
        a=x
    n=n//10
print(a)
n = int(input("N = "))
m = int(input("M = "))
s = 0
while n <= m:
    i = 2
    k = 0
    while i < n:
        if n % i == 0:
            k = 1
        i = i + 1
    if n > 1 and k == 0:
        s = s + 1
    n = n + 1
print(s)
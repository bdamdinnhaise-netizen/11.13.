n = int(input("N = "))
i = 1
s = 0
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        s = s + 1
    i = i + 1
print(s)
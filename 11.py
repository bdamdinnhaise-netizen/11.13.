n = int(input("N = "))
s = 0
i = 1

while i <= n:
    if i % 5 == 0:
        s = s + i
    i = i + 1

print(s)
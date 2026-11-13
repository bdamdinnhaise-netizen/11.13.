n = int(input("n = "))
a = n
i = 0
while i <= 9:
    s = 0
    n = a
    while n > 0:
        if n % 10 == i:
            s = s + 1
        n = n // 10
    print(i, s)
    i = i + 1
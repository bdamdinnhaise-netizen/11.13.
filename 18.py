n = int(input("n = "))
i = 2
s = 0
while i < n:
    if n % i == 0:
        s = 1
    i = i + 1
if n > 1 and s == 0:
    print("Anhnii too")
else:
    print("Anhnii too bish")
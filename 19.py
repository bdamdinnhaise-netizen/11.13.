n = int(input("n = "))
a = n
s = 0
while n > 0:
    s = s * 10 + n % 10
    n = n // 10
if a == s:
    print("Adil")
else:
    print("Adil bish")
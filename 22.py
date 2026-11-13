n = int(input("n = "))
ih = 0
baga = 9
while n > 0:
    a = n % 10
    if a > ih:
        ih = a
    if a < baga:
        baga = a
    n = n // 10
print(ih)
print(baga)
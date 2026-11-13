# # a = ["gcy", "ykn","zulbasag"]
# # print (max(a))

# # a = ["gcy", "ykn","zulbasag"]
# # print (min(a))

# # a = ["gcy", "ykn","zulbasag"]
# # urt = (max(a, key = len))
# # print (urt.upper())

# # a = ["gcy", "ykn","zulbasag"]
# # urt = (max(a, key = len))
# # print (urt.lower())

# a = ["gcy", "ykn","zulbasag"]
# bogino = (min(a, key = len))
# a[a.index(bogino)] = "sain uu"
# print (a)

# a = [1,2,3,4,5]
# a.sort(reverse=True)
# print (a)

# a = [1,2,3,4,5]
# ih = [a.index(max(a))]
# baga = [a.index(min(a))]
# a[ih[0]] , a[baga[0]] = a[baga[0]] , a[ih[0]]
# print(a) 

# for i in range(1, 10):
#     if i * i > 100:
#         break
#     print(i * i)

# for i in range(1, 100):
#     if i % 3 != 0 or i % 5 != 0:
#         continue
#     print(i)

# n = int(input("too oruulna uu: "))
# if n < 2:
#     print("Anhnii too bish")
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print("Anhnii too bish")
#             break
#     else:
#             print(n, "Anhnii too")
            
# too = list(range(1, 51))
# print(too)


# a = [1,2,3,4,5]
# a.sort(reverse=True)
# print(a)


# truple

# too = (5, 2, 3, 4, 9)
# s = sum(too)
# print("niilber: ", s)

# ner = ("gcy", "ykn", "zulbasag")
# urt = (max(ner, key = len))
# print("hamgin urt ner: ", urt)

# too = (5, 2, 3, 4, 9)
# print ("ih too: ", max(too))
# print ("baga too: ", min(too))

# too = (5, 2, 3, 4, 9)
# for i in too:
#     if i % 2 == 0:
#         print(i, "bolon tegsh too")
#     else:
#         print(i, "bolon sondgoi too")
        
# too = (5, 10, 8, 4, 9)
# for i in too:
#             print("10 baina")
            
# else:
#             print("10 baihgui") 
                
                
# firstset = {1, 2, 3, 4, 5 , 1}
# firstset.discard (1)
# print(firstset)


# firstset = {1, 9, 3, 4, 5,7,9}
# firstset.add(2)
# firstset.remove(9)
# print(firstset)

surr = {"bat": [80, 90], "sarnai": [95,98]}
top = max(surr, key=lambda s: sum(surr[s]) / len(surr[s]))
print("shildg:", top)
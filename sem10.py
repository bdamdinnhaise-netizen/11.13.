# import numpy as np
# array=np.array([1,2,3,4,5])
# print(array)


# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr)


# import numpy as np
# arr=np.array([
#     [[1,2,3],
#      [6,7,8]],
#     [[1,2,3],
#      [6,7,8]]
# ])
# print(arr)


# import numpy as np
# arr=np.array([3,2,0,1])
# print(np.sort(arr))

# import numpy as np
# arr=np.array(["blue","green","red"])
# print(np.sort(arr))


# import numpy as np
# arr=np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ])
# print(np.sort(arr))


# import numpy as np
# array = np.array([1, 2, 3, 4, 5])
# print("Дундаж:", np.mean(array))
# print("Нийлбэр:", np.sum(array))
# print("Хамгийн их:", np.max(array))
# print("Хамгийн бага:", np.min(array))

# import numpy as np
# arr = np.arange(0, 12)
# arr = arr.reshape(3, 4)
# print(arr)


# import numpy as np 
# a = np.arange(1,15)
# print(a[a>5])


# import numpy as np
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print("Мөрийн нийлбэр:")
# print(np.sum(arr, axis=1))
# print("Баганын дундаж:")
# print(np.mean(arr, axis=0))


# import numpy as np
# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.mean(arr,axis=1))
# print(np.sum(arr))
# print(np.max(arr))
# print(np.min(arr))


# import numpy as np
# arr = np.arange(1,21)
# print(arr[arr%2==1])
# print(np.sum(arr))
# print(np.mean(arr))


# import numpy as np
# arr=np.random.randint(1,11,10)
# print(arr)
# print(arr[arr>5])
# arr[arr<5]=0
# print(arr)


# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr[2:5])


# import numpy as np
# arr=np.array(["apple","banana","cat","dog"])
# print(len(arr))
# print(min(arr))
# print(max(arr))
# print(",".join(arr))


# import numpy as np
# arr=np.array([12,7,25,18,30,9,14,21])
# print(arr[arr%2==0])
# print(arr[arr%2==1])
# print(np.sum(arr[arr%2==0]))
# print(np.sum(arr[arr%2==1]))

# import numpy as np

# arr=np.array([65,78,90,55,88,72,95,60,83,47])

# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(arr[arr>70])
# print(arr[arr<60])
# print(np.sort(arr))


# import numpy as np

# arr=np.array([
#     [12,15,18],
#     [20,25,30],
#     [10,14,16]
# ])

# print(np.sum(arr,axis=1))
# print(np.mean(arr,axis=0))
# print(np.max(arr))
# print(np.sum(arr))


import numpy as np

arr=np.array([250,320,180,400,350,500,280])

print(np.sum(arr))
print(np.mean(arr))
print(np.argmax(arr)+1)
print(arr[arr>300])

newarr=arr*1.1
print(newarr)
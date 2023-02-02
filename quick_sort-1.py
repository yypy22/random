

import random

num = 15
data = [0]*num

for i in range(num):
    data[i] = random.randint(100,199)

def quick(left, right):
    i = left
    j = right
    pivot = data[(left+right)//2]
    while True:
        while data[i] < pivot:
            i = i+1
        while data[j] > pivot:
            j = j-1
            if i >= j:
                break
            data[i], data[j] = data[j], data[i]
            i = i+1
            j = j-1
    if left <i-1:
        quick(left, i-1)
    if right > j+1:
        quick(j+1, right)

a = quick(0,14)
print(a, "sorted")


























































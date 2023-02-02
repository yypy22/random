

data = [11,23,43,33,56,23,67,89,56,60,71,58,89,90]

num = len(data)

for i in range(num):
    tmp = data[i]
    j = i
    while j>0 and data[j-1] > tmp:
        data[j] = data[j-1]
        j = j-1
        data[j] = tmp

print(data, "sorted")




























































data = [11,23,43,33,56,23,67,89,56,60,71,58,89,90]

num = len(data)

for i in range(num-1):
    for j in range(num-1,i,-1):
        if data[j-1] > data[j]:
            data[j],data[j-1] = data[j-1], data[j]

print(data,"sorted")












































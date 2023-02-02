



data = [11,23,43,33,56,23,67,89,56,60,71,58,89,90]

for i in range(len(data)):
    mini = i
    for j in range(i+1, len(data)):
        if data[j] < data[mini]:
            mini = j
        data[i], data[mini] = data[mini], data[i]

print(data, "sorted")














































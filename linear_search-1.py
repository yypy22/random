#linear search 





data = [11,23,43,33,56,23,67,89,56,60,71,58,89,90]

num = len(data)
key = 60
bo = False
i = 0
while i<num and data[i]!=key:
    i +=1
if num != i:
    print("there is key value in data")
else:
    print("no key")


















































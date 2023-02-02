
#bin search

data = [11,23,43,33,56,23,67,89,56,60,71,58,89,90]
key = 58
left = 0
right = len(data) -1
bo = False
while left <= right:
    mid = (left+right)//2
    if data[mid] == key:
        bo = True
        break
    if data[mid] < key:
        left = mid+1
    if data[mid] > key:
        right = mid-1
if bo == False:
    print("no key in data")








































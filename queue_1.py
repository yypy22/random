
# queue

MAX = 11
queue = [0]*MAX

head = 0
tail = 0

def push(data):
    global tail
    posision = (tail+1)%MAX

    if posision != head:
        queue[tail] = data
        tail = posision

def pop():
    global head

    if head != tail:
        data = queue[head]
        head = (head+1)%MAX
        return data
    else:
        return None

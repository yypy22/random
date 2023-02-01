
#Stack 

MAX_SIZE = 10
stack = [0]*MAX_SIZE
stack_pointer = 0

def push(data):
    global stack_pointer

    if stack_pointer < MAX_SIZE:
        stack[stack_pointer] = data
        stack_pointer += 1

def pop():
    global stack_pointer
    if stack_pointer > 0:
        stack_pointer -= 1
        return stack[stack_pointer]

for i in range(11):
    push(i)
for j in range(11):
    datas = pop()
    print(datas)


#tree search

node = [
    [1,2,10],
    [3,4,5],
    [5,None,12],
    [None,None,2],
    [6,7,8],
    [None,None,11],
    [None,None,6],
    [None,None,9]
]
left = 0
right = 1
data =2
def tree(point):
    if point != None:
        tree(node[point][left])
        print(node[point][data])
        tree(node[point][right])
        tree(0)
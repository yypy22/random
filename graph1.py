#graph


data = [
    [1,1,0,0,0],
    [0,1,1,0,0],
    [1,1,0,0,1],
    [0,0,1,1,1],
    [1,0,0,1,1],
]

nodes = ["0", "1", "2", "3", "4"]

for i in range(5):
    for j in range(i,5):
        if data[i][j] == 1 and data[j][i] ==1:
            print(nodes[i] +"<->"+nodes[j])


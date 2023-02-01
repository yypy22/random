data = [
    [1,1,0,0,0],
    [0,1,1,0,0],
    [1,1,0,0,1],
    [0,0,1,1,1],
    [1,0,0,1,1],
]

nodes = ["0", "1", "2", "3", "4"]

ar = ["", "-->", "<--", "<-->"]

for i in range(5):
    for j in range(i,5):
        a = data[i][j]
        b = data[j][i]
        c = a+b*2
        if c > 0:
            print(nodes[i]+ar[c]+nodes[j])

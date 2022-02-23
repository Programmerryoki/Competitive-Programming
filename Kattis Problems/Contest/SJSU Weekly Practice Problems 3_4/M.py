board = [list(input()) for i in range(8)]
T = [7,0]
D = []
for i,a in enumerate(board):
    if "D" in a:
        D = [i, a.index("D")]
        break

map = [[0]*8 for i in range(8)]
queue = []
moveable = [[-1,0],[0,-1],[1,0],[0,1]]

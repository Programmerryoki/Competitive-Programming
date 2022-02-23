R, C = [int(i) for i in input().split()]
matrix = []
for a in range(R):
    matrix.append(input())

col = ["".join([line[i] for line in matrix]) for i in range(C)]
c = -1
while len(set(col)) == len(col):
    col = [i[1:] for i in col]
    c += 1
print(c)
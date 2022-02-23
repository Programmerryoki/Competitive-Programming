line = input()
C = len(line)
for i in range(int(len(line)**0.5), 0, -1):
    if len(line)%i == 0:
        C = i
        break
R = len(line)//C
# print(R,C)
matrix = [[""]*C for i in range(R)]
for i,w in enumerate(line):
    matrix[i//C][i%C] = w
print("".join("".join(i[j] for i in matrix) for j in range(C)))
cor = 0
time = 0
right = []
wrong = []

while True:
    line = input()
    if line == "-1":
        break

    line = line.split()
    pos = [i[0] for i in wrong]
    if line[2] == "right":
        right.append(line[1])
        time += int(line[0])
        if line[1] in pos:
            time += 20 * wrong[pos.index(line[1])][1]
        cor += 1
    else:
        if line[1] in pos:
            wrong[pos.index(line[1])][1] += 1
        else:
            wrong.append([line[1], 1])
print(cor,time)
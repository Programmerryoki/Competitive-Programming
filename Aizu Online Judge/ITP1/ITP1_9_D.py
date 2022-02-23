s = list(input())
q = int(input())
for _ in range(q):
    line = input().split()
    if line[0][2] == "p":
        s = s[:int(line[1])] + list(line[3]) + s[int(line[2])+1:]
    elif line[0][2] == "v":
        s = s[:int(line[1])] + s[int(line[1]):int(line[2])+1][::-1] + s[int(line[2])+1:]
    elif line[0][0] == "p":
        print("".join(s[int(line[1]):int(line[2])+1]))
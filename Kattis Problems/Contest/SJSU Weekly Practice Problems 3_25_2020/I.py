t = int(input())
for _ in range(t):
    print("3 1 3 6",flush=True)
    while True:
        line = input().split()
        if line[0] == "GAME":
            break
        line = [int(i) for i in line[1:]]
        line[3], line[1] = 7 - line[1], 7 - line[3]
        line[2], line[0] = 6 - line[0], 6 - line[2]
        print(" ".join(map(str, line)), flush=True)
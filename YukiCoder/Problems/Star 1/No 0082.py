W,H,C = input().split()
for i in range(int(H)):
    for j in range(int(W)):
        print("BW"[(i+j)%2] if C == "B" else "WB"[(i+j)%2], end = "")
    print()
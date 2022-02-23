H,W = map(int, input().split())
for i in range(H):
    line = input().split()
    if "snuke" in line:
        print(chr(ord("A")+line.index("snuke"))+str(i+1))
        exit()
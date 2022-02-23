n = input().split()
d = (int(n[1])**2 + int(n[2])**2)**0.5
for a in range(int(n[0])):
    length = int(input())
    if length <= d:
        print("DA")
    else:
        print("NE")
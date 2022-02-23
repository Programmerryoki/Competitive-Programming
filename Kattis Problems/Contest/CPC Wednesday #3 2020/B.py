T = int(input())
for a in range(T):
    s = input()
    ng, nm = [int(i) for i in input().split()]
    g = max([int(i) for i in input().split()])
    m = max([int(i) for i in input().split()])
    if g >= m:
        print("Godzilla")
    else:
        print("MechaGodzilla")
N = int(input())
cup = []
for a in range(N):
    s = input().split()
    try:
        num = int(s[0])
        cup.append([num/2, s[1]])
    except:
        cup.append([int(s[1]), s[0]])
cup.sort()
for a in cup:
    print(a[1])
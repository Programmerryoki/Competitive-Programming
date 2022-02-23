S = input()
K = int(input())
for s in S:
    if s == "1":
        K -= 1
    else:
        print(s)
        break
    if K == 0:
        print(s)
        break
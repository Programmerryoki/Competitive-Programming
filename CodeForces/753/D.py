t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    color = input()
    R,B = [],[]
    for i,a in enumerate(A):
        if color[i] == "R":
            R.append(a)
        else:
            B.append(a)
    R.sort()
    B.sort()
    # print(R,B)
    for i in range(len(B)):
        if i+1 > B[i]:
            print("NO")
            break
    else:
        for i in range(len(R)):
            if i+len(B)+1 < R[i]:
                print("NO")
                break
        else:
            print("YES")
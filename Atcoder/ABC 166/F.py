N,A,B,C = [int(i) for i in input().split()]
ans = []
for _ in range(N):
    s = input()
    if s[0] == "A" and s[1] == "B":
        if A < B:
            A += 1
            B -= 1
            ans.append("A")
        else:
            A -= 1
            B += 1
            ans.append("B")
    elif s[0] == "A" and s[1] == "C":
        if A < C:
            A += 1
            C -= 1
            ans.append("A")
        else:
            A -= 1
            C += 1
            ans.append("C")
    elif s[0] == "B" and s[1] == "C":
        if B < C:
            B += 1
            C -= 1
            ans.append("B")
        else:
            B -= 1
            C += 1
            ans.append("C")
    if min(A,B,C) < 0:
        print("No")
        break
else:
    print("Yes")
    print("\n".join(ans))
N,A,B = [int(i) for i in input().split()]
S = input()
ans = []*N
b = 0
a = 0
for i in S:
    if i == "a" and a+b < A+B:
        a += 1
        ans.append("Yes")
        continue
    elif i == "b" and a+b < A+B and b < B:
        b += 1
        ans.append("Yes")
        continue
    ans.append("No")
print("\n".join(ans))
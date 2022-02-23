s = list(input())
back = len(s)-1
while back >= 0 and s[back] != ")":
    back -= 1
front = 0
while front < len(s) and s[front] != "(":
    front += 1
ans = []
i = 0
while len(s) != 0:
    # print(s)
    bf = []
    bb = []
    # print("in loop")
    while front <= back:
        if s[front] == "(":
            bf.append(front)
        if s[back] == ")":
            bb.append(back)
        front += 1
        back -= 1
        while front < len(s) and s[front] != "(":
            front += 1
        while back >= 0 and s[back] != ")":
            back -= 1
        # print(front, back)
    if len(bf) > len(bb):
        bf = bf[:len(bb)]
    else:
        bb = bb[:len(bf)]
    bb.sort()
    n = bf+bb
    # print(n)
    for a in n[::-1]:
        del s[a]
    if len(n) != 0:
        ans.append(n)
    else:
        break

print(len(ans))
for a in ans:
    print(len(a))
    print(" ".join(map(lambda x: str(x+1), a)))

# s = input()
# n = 0
# j = 0
# last = 0
# ans = []
# for i,a in enumerate(s):
#     if a == "(":
#         n += 1
#     else:
#         n -= 1
#         if j != i:
#             ans.append(j+1)
#             ans.append(i+1)
#         j += 1
#         while j < len(s) and s[j] != "(":
#             j += 1
#     if n == 0:
#         last = i
# if len(ans) == 0:
#     print(0)
# else:
#     print(ans)
#     ans.sort()
#     print(1)
#     print(len(ans))
#     print(" ".join(map(str, ans)))
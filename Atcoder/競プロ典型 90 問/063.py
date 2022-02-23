from collections import defaultdict

H,W = [int(i) for i in input().split()]
P = [[int(i) for i in input().split()] for j in range(H)]
maxg = 1
for n in range(1,2**H):
    choose = bin(n)[2:]
    choose = "0"*(H - len(choose)) + choose
    nums = defaultdict(int)
    mn = 0
    for i in range(W):
        num = float("inf")
        for j in range(H):
            if choose[j] != "1":
                continue
            if num == float("inf"):
                num = P[j][i]
            elif num != P[j][i]:
                break
        else:
            nums[num] += 1
            if nums[num] > mn:
                mn = nums[num]
    g = choose.count("1") * mn
    if g > maxg:
        maxg = g
print(maxg)
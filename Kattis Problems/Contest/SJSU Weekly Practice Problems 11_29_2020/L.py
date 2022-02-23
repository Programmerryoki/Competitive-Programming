import re

P = int(input())
for _ in range(P):
    K, *rest = [int(i) for i in input().split()]
    count = 0
    il = [rest]
    while il:
        # print(il)
        temp = il.pop()
        nums = " ".join([str(i) if i != 0 else " " for i in temp]).strip()
        # print(nums)
        nums = re.split(r"\s\s+", nums)
        # print("\t",nums)
        for line in nums:
            if not line:
                continue
            # print("line : ",line)
            t = [int(j) for j in line.split()]
            # print(t)
            mi = min(t)
            for i in range(len(t)):
                t[i] -= mi
            count += 1
            il.append(t)
            # print(t)
    print(K,count)
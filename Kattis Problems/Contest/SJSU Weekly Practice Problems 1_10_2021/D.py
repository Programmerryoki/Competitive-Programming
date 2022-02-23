b,d,c,l = map(int, input().split())
nums = []
for i in range(l//b + 1):
    for j in range(l//d + 1):
        sd = i*b + j*d
        if sd > l:
            break
        for k in range(l//c + 1):
            sums = i*b + j*d + k*c
            if sums == l:
                nums.append((i,j,k))
            elif sums > l:
                break
if not nums:
    print("impossible")
    exit()

nums.sort()
print("\n".join(" ".join(map(str, i)) for i in nums))
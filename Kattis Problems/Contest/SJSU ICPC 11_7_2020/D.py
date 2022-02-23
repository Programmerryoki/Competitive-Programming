from bisect import bisect_right

H = []
while True:
    line = int(input())
    if line == 0:
        break
    H.append(line)
mh = max(H)
hcom = []
ha = set()
for a in range(1,250001):
    if 16*a**2+8*a+1 > mh:
        break
    if 4*a+1 in ha:
        continue
    for b in range(a,250001):
        if 4*b+1 in ha:
            continue
        num = 16*a*b+4*(a+b)+1
        if num > mh:
            break
        for com in hcom:
            if num%com == 0:
                print(4*a+1, 4*b+1)
                print(num, com)
                break
        else:
            hcom.append(num)
            ha.add(num)
hcom.sort()
print(hcom)
print("\n".join(" ".join(map(str, [i,bisect_right(hcom, i)])) for i in H))
L,R = map(int, input().split())
if R - L > 2019:
    print(0)
elif R // 2019 != L // 2019:
    print(0)
else:
    minv = 2020
    for i in range(L, R):
        for j in range(i+1, R+1):
            minv = min(minv, (i*j) % 2019)
    print(minv)
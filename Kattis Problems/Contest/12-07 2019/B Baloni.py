N = int(input())
H = [int(i) for i in input().split()]

h = []
j = 0

while j < len(H):
    # print(h,j,H[j])
    try:
        i = h.index(H[j])
        h[i] -= 1
    except:
        h.append(H[j]-1)
    j += 1
print(len(h))
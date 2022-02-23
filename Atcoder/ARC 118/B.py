K,N,M = map(int, input().split())
mul = 10**55
A = [int(i) for i in input().split()]
Bs = [i * M * mul / N for i in A]
B = [int(i / mul) for i in Bs]
sorting = [(j%mul,i) for i,j in enumerate(Bs)]
sorting.sort(key=lambda x: (-x[0], x[1]))
# print(Bs)
# print(B)
# print(sorting)
for i in range(max(0, M - sum(B))):
    B[sorting[i][1]] += 1
print(" ".join(map(str, B)))
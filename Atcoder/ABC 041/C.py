N = int(input())
A = [(int(j), i) for i,j in enumerate(input().split())]
A.sort(reverse=True)
print("\n".join(map(str, [i[1]+1 for i in A])))
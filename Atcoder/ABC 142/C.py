N = int(input())
A = [[int(n), i] for i,n in enumerate(input().split(), 1)]
A.sort()
print(" ".join(map(str, [i[1] for i in A])))
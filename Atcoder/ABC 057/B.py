N,M = [int(i) for i in input().split()]
student = [[int(i) for i in input().split()] for j in range(N)]
check = [[int(i) for i in input().split()] + [j+1] for j in range(M)]
print("\n".join(map(str, [min(check, key=lambda x: abs(i[0] - x[0]) + abs(i[1] - x[1]))[-1] for i in student])))
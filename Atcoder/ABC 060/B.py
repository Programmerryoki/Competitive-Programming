A, B, C = [int(i) for i in input().split()]
rem = set()
for i in range(1,B+1):
    rem.add((A*i)%B)
print("YES" if C in rem else "NO")
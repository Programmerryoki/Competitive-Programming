A,B = [int(i) for i in input().split()]
ans = [i for i in range(1,A+B*5+1)]
if A < 4:
    ans = [i for i in ans if i%5 <= A]
print("\n".join(map(str, ans)))
s = 0
for n in range(1001):
    s += sum([int(i) for i in str(n)])
    print(n,s,)

# for _ in range(int(input())):
#     a,b = map(int, input().split())
#
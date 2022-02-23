n = int(input())
ppl = [int(i) for i in input().split()]
order = [0]*n
order[0] = 1
for i in range(2,n+1):
    order[ppl[i - 2]+1] = i
print(" ".join(map(str, order)))
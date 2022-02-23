num = 10**9+1
def optimal(lst, k):
    a = (lst.copy())[::-1]
    for i in range(len(a) - k):
        a[a.index(min(a))] = num
    return [i for i in a if i != num][::-1]


n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
requests = [[int(i) for i in input().split()] for j in range(m)]
# print(requests)
digs = set([i[0] for i in requests])
# print(digs)
op = {}
for i in range(len(digs)):
    k = digs.pop()
    seq = optimal(a, k)
    op[k] = seq

for req in requests:
    # print(req)
    # print(op[req[0]])
    print(op[req[0]][req[1]-1])
from heapq import heappush, heappop

mc = []
while True:
    cs = []
    try:
        while True:
            l = input()
            if l == '':
                break
            cs.append(int(l))
    except:
        break
    heappush(mc, -sum(cs))
s = [-heappop(mc) for _ in range(3)]
print(sum(s))
import heapq

X,Y,A,B,C = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]
R = [-int(i) for i in input().split()]
P.sort()
Q.sort()
total = P[A-X:] + Q[B-Y:]
total.sort()
heapq.heapify(R)
i = 0
while True:
    try:
        n = -heapq.heappop(R)
        if i < len(total) and total[i] < n:
            total[i] = n
            i += 1
        else:
            break
    except:
        break
print(sum(total))
price = [0]+[int(i) for i in input().split()]
times = [0]*100
for _ in range(3):
    arr, dep = map(int, input().split())
    for i in range(arr-1, dep-1):
        times[i] += 1
cost = 0
for i in times:
    cost += price[i]*i
print(cost)
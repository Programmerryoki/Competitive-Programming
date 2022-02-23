n, m = [int(i) for i in input().split()]
stations = []
votes = [0 for i in range(n)]
for a in range(m):
    s = [int(i) for i in input().split()]
    for i in range(n):
        votes[i] += s[i]
    stations.append(s)
poll = [i[-1] for i in stations]
# print(votes)
# print(stations)
# print(poll)
c = 0
re = []
while votes[-1] > max(votes[:-1]):
    index = poll.index(max(poll))
    poll[index] = 0
    re.append(index+1)
    cancel = stations[index]
    for i in range(n):
        votes[i] -= cancel[i]
    c += 1
print(c)
print(" ".join(map(str, re)))
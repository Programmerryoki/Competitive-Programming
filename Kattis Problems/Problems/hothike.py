n = int(input())
days = [int(i) for i in input().split()]
day = [max(days)+1, max(days)+1]
d = 0
for a in range(len(days)-2):
    if max(day) > max(days[a],days[a+2]):
        day = [days[a],days[a+2]]
        d = a+1
print(d, max(day))
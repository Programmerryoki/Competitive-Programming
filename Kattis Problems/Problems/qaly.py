n = int(input())
total = 0
for a in range(n):
    qaly = input().split(" ")
    total += float(qaly[0])*float(qaly[1])
print(total)
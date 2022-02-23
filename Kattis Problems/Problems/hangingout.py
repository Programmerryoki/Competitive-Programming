L, x = [int(i) for i in input().split()]
current = 0
reject = 0
for a in range(x):
    group = input().split()
    if group[0] == "enter":
        if current + int(group[1]) <= L:
            current += int(group[1])
        else:
            reject += 1
    elif group[0] == "leave":
        current -= int(group[1])
print(reject)
n, k = [int(i) for i in input().split()]
system = [[-1000]*k]
for a in range(n):
    t = int(input())
    for s in range(len(system)):
        for i in range(len(system[s])):
            if t - system[s][i] >= 1000:
                system[s][i] = t
                break
        else:
            continue
        break
    else:
        system.append([t]*k)
print(len(system))
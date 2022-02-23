from fractions import gcd

n = int(input())
gear = [[[int(i) for i in input().split()]+[0]]]
for _ in range(n-1):
    x,y,r = [int(i) for i in input().split()]
    c = 0
    d = -1
    connect = []
    valid = [True]
    for i,ge in enumerate(gear):
        for g in ge:
            if ((x - g[0])**2 + (y - g[1])**2)**0.5 == r + g[2]:
                if d == -1:
                    d = 1 - g[3]
                elif d == g[3]:
                    print("-1")
                    valid[i] = False
                    break
            else:
                c += 1
                if c == len(gear):
                    break
        else:
            connect.append(i)
            continue
        break
    if len(connect):
        first = connect[0]
        connect = connect[1:]
        for a in connect[::-1]:
            gear[first] += gear.pop(a)
            del valid[a]
        gear[first].append([x,y,r,d])
    else:
        gear.append([[x,y,r,d]])
        valid.append(True)
    if not valid[0]:
        break

print(gear)
print(valid)

if valid[0]:
    source = gear[0][0]
    target = gear[-1][-1]
    s = source[2]
    t = target[2]
    g = gcd(s,t)
    s, t = s//g, t//g
    if source[-1] == target[-1]:
        print(t,s)
    else:
        print(t,-s)
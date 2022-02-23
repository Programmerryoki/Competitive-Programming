N = int(input())
colors = "RGB"
dogs = {"R":[],"G":[],"B":[]}
for _ in range(2*N):
    a,c = input().split()
    dogs[c].append(int(a))
first, second, third = None, None, None
for color in colors:
    if len(dogs[color])&1:
        if not first:
            first = dogs[color]
        else:
            second = dogs[color]
    else:
        third = dogs[color]
if not first and not second:
    print(0)
    exit()
first.sort()
second.sort()
third.sort()

def mindiff(first, second):
    mindif = float("inf")
    ai = 0
    bi = 0
    while ai < len(first) and bi < len(second):
        dif = abs(first[ai] - second[bi])
        if dif < mindif:
            mindif = dif
        if first[ai] < second[bi]:
            ai += 1
        elif first[ai] > second[bi]:
            bi += 1
        else:
            if ai < bi:
                ai += 1
            else:
                bi += 1
    return mindif

dif1 = mindiff(first, second)
dif2 = mindiff(first,third)
dif3 = mindiff(second, third)
print(min(dif1, dif2+dif3))
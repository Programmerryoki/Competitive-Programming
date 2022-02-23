from sys import stdin
from math import atan2

input = stdin.readline
origin = (400,400)

def angle(p1, p2):
    return atan2(p2[0]-p1[0], p2[1]-p1[1])

def main():
    positions = [[int(i) for i in input().split()] for _ in range(1000)]
    starts = []
    ends = {}
    for i,[a,b,c,d] in enumerate(positions):
        starts.append(((a,b),angle(origin, (a,b)),i))
        ends[i] = ((c,d),angle(origin, (c,d)))
    starts.sort()
    ans_ind = []
    ans_coord = [(400,400)]
    for i in range(50):
        ans_ind.append(starts[i][-1] + 1)
        ans_coord.append(starts[i][0])
    for i in range(50):
        ans_coord.append(ends[ans_ind[i]-1][0])
    ans_coord.append((400,400))
    print(len(ans_ind)," ".join(map(str, ans_ind)))
    print(len(ans_coord)," ".join(" ".join(map(str,i)) for i in ans_coord))


if __name__ == '__main__':
    main()
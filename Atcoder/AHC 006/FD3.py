from sys import stdin
from math import atan2

input = stdin.readline
origin = (400,400)

def angle(p1, p2):
    return atan2(p2[0]-p1[0], p2[1]-p1[1])

def dist(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5

def main():
    positions = [[int(i) for i in input().split()] for _ in range(1000)]
    starts = []
    ends = {}
    for i,[a,b,c,d] in enumerate(positions):
        starts.append({"dist":dist(origin,(a,b)),"coord":(a,b),"angle":angle(origin, (a,b)),"index":i})
        ends[i] = {"dist":dist(origin,(c,d)),"coord":(c,d),"angle":angle(origin, (c,d))}
    starts.sort(key = lambda x: (x["dist"]+ends[x["index"]]["dist"],x["coord"]))
    starts = starts[:50]
    starts.sort(key = lambda x: (x["angle"],x["dist"]))
    ans_ind = []
    ans_coord = [(400,400)]
    for i in range(50):
        ans_ind.append(starts[i]["index"]+1)
        ans_coord.append(starts[i]["coord"])
    end_tmp = [ends[i-1] for i in ans_ind]
    end_tmp.sort(key=lambda x: (x["angle"],x["dist"]))
    for i in range(50):
        ans_coord.append(end_tmp[i]["coord"])
    ans_coord.append((400,400))
    print(len(ans_ind)," ".join(map(str, ans_ind)))
    print(len(ans_coord)," ".join(" ".join(map(str,i)) for i in ans_coord))


if __name__ == '__main__':
    main()
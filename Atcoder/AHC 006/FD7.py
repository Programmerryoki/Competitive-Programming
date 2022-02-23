from sys import stdin
from math import atan2
from copy import deepcopy

input = stdin.readline
origin = (400,400)

def score(path):
    total = 0
    cur = path[0]
    for i in path[1:]:
        total += (abs(cur[0]-i[0]) + abs(cur[1]-i[1]))
        cur = i
    return total

def angle(p1, p2):
    return atan2(p2[0]-p1[0], p2[1]-p1[1])

def dist(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5

def optimize(path):
    while True:
        change = False
        for i in range(len(path)-4):
            if i == 49:
                continue
            a,b,c,d = path[i],path[i+1],path[i+2],path[i+3]
            if dist(a,b)+dist(c,d) > dist(a,c)+dist(b,d):
                path[i+1],path[i+2] = path[i+2],path[i+1]
                change = True
        if not change:
            break
    return path

def best_path(starts, ends, ori):
    mind = float("inf")
    ansi = []
    ansc = []
    for offset in range(50):
        ans_ind = []
        ans_coord = [(400,400)]
        if ori != origin:
            ans_coord.append(ori)
        for i in range(50):
            ans_ind.append(starts[(i+offset)%50]["index"]+1)
            ans_coord.append(starts[(i+offset)%50]["coord"])
        end_tmp = [ends[i-1] for i in ans_ind]
        end_tmp.sort(key=lambda x: (x["angle"],x["dist"]))
        for i in range(50):
            ans_coord.append(end_tmp[(i+offset)%50]["coord"])
        ans_coord.append((400,400))
        ans_coord = optimize(ans_coord)
        tmp = score(ans_coord)
        if tmp < mind:
            mind = tmp
            ansi = ans_ind
            ansc = ans_coord
    return ansi, ansc, mind

def adjust(starts, ends, ori):
    for i in range(len(starts)):
        starts[i]["dist"] = dist(starts[i]["coord"],ori)
    for i in ends:
        ends[i]["dist"] = dist(ends[i]["coord"], ori)

def search1(starts, ends, ori):
    adjust(starts, ends, ori)
    starts.sort(key = lambda x: (x["dist"]+ends[x["index"]]["dist"],x["coord"]))
    starts = starts[:50]
    starts.sort(key = lambda x: (x["angle"],x["dist"]))
    return best_path(starts, ends, ori)

def search3(starts, ends, ori):
    adjust(starts, ends, ori)
    starts.sort(key = lambda x: (x["dist"]*ends[x["index"]]["dist"],x["coord"]))
    starts = starts[:50]
    starts.sort(key = lambda x: (x["angle"],x["dist"]))
    return best_path(starts, ends, ori)

def search6(starts, ends, ori):
    adjust(starts, ends, ori)
    starts.sort(key = lambda x: (x["dist"]-ends[x["index"]]["dist"],x["coord"]))
    starts = starts[:50]
    starts.sort(key = lambda x: (x["angle"],x["dist"]))
    return best_path(starts, ends, ori)

def search7(starts, ends, ori):
    adjust(starts, ends, ori)
    starts.sort(key = lambda x: (ends[x["index"]]["dist"]-x["dist"],x["coord"]))
    starts = starts[:50]
    starts.sort(key = lambda x: (x["angle"],x["dist"]))
    return best_path(starts, ends, ori)

def main():
    positions = [[int(i) for i in input().split()] for _ in range(1000)]
    starts = []
    ends = {}
    for i,[a,b,c,d] in enumerate(positions):
        starts.append({"dist":dist(origin,(a,b)),"coord":(a,b),"angle":angle(origin, (a,b)),"index":i})
        ends[i] = {"dist":dist(origin,(c,d)),"coord":(c,d),"angle":angle(origin, (c,d))}

    searches = [search1, search3, search6, search7]
    ms = float("inf")
    tmp = deepcopy(starts)
    tmp.sort(key=lambda x: (x["dist"]))
    coords = [origin]+[i["coord"] for i in tmp[10:140:5]]
    indexes = []
    path = []
    for func in searches:
        for i in range(len(coords)):
            tmp1, tmp2, t = func(deepcopy(starts), deepcopy(ends), coords[i])
            if t < ms:
                ms = t
                path = tmp2
                indexes = tmp1
    print(len(indexes)," ".join(map(str, indexes)))
    print(len(path)," ".join(" ".join(map(str,i)) for i in path))


if __name__ == '__main__':
    main()
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

def search1(starts, ends):
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
    return ans_ind, optimize(ans_coord)

def search2(starts, ends):
    starts.sort(key = lambda x: (x["dist"],x["coord"]))
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
    return ans_ind, optimize(ans_coord)

def search3(starts, ends):
    starts.sort(key = lambda x: (x["dist"]*ends[x["index"]]["dist"],x["coord"]))
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
    return ans_ind, optimize(ans_coord)

def search4(starts, ends):
    starts.sort(key = lambda x: (x["dist"]/ends[x["index"]]["dist"],x["coord"]))
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
    return ans_ind, optimize(ans_coord)

def search5(starts, ends):
    starts.sort(key = lambda x: (ends[x["index"]]["dist"]/x["dist"],x["coord"]))
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
    return ans_ind, optimize(ans_coord)

def search6(starts, ends):
    starts.sort(key = lambda x: (x["dist"]-ends[x["index"]]["dist"],x["coord"]))
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
    return ans_ind, optimize(ans_coord)

def search7(starts, ends):
    starts.sort(key = lambda x: (ends[x["index"]]["dist"]-x["dist"],x["coord"]))
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
    return ans_ind, optimize(ans_coord)

def main():
    positions = [[int(i) for i in input().split()] for _ in range(1000)]
    starts = []
    ends = {}
    for i,[a,b,c,d] in enumerate(positions):
        starts.append({"dist":dist(origin,(a,b)),"coord":(a,b),"angle":angle(origin, (a,b)),"index":i})
        ends[i] = {"dist":dist(origin,(c,d)),"coord":(c,d),"angle":angle(origin, (c,d))}

    searches = [search1, search2, search3, search4, search5, search6, search7]
    ms = float("inf")
    indexes = []
    path = []
    for func in searches:
        tmp1, tmp2 = func(deepcopy(starts), deepcopy(ends))
        t = score(tmp2)
        if t < ms:
            ms = t
            path = tmp2
            indexes = tmp1
    print(len(indexes)," ".join(map(str, indexes)))
    print(len(path)," ".join(" ".join(map(str,i)) for i in path))


if __name__ == '__main__':
    main()
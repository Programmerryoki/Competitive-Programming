from sys import stdin
from bisect import bisect_left

def main():
    input = stdin.readline

    n,m = map(int, input().split())
    scored = {1:0}
    scores = [[0,0,1]]
    rank = [0]*m
    for event in range(m):
        t,p = map(int, input().split())
        if t in scored:
            tmp = scores[scored[t]]
            tmp[0] += 1
            tmp[1] += p
            scores.sort(key=lambda x: (-x[0],x[1],x[2]))
            place = [i[-1] for i in scores]
            for i,t in enumerate(place):
                scored[t] = i
        else:
            tmp = [1,p,t]
            index = bisect_left(scores, [-1, -p, t])
            scores.insert(index, tmp)
            scored[t] = index
            place = [i[-1] for i in scores]
            for i,t in enumerate(place[index:]):
                scored[t] = i
        rank[event] = scored[1] + 1
    print("\n".join(map(str, rank)))

if __name__ == "__main__":
    main()
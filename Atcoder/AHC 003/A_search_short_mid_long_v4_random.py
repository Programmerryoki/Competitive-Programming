# A_search_short_mid_long try to catch as many inf as it can + margin
from sys import stdin
from heapq import heappush, heappop
from random import randint
from itertools import accumulate

def main():
    input = stdin.readline
    path_length = {(i,j):[float("inf")]*4 for i in range(30) for j in range(30)}
    moves = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
    opp_moves = {"U":"D","D":"U","L":"R","R":"L"}
    dir = "UDLR"
    amoves = [(-1,0),(1,0),(0,-1),(0,1)]

    def update_path_length(i,j,path, len_path, path_length):
        unit_path = len_path / len(path)
        pos = (i,j)
        for move in path:
            dx,dy = moves[move]
            x,y = pos[0]+dx,pos[1]+dy
            txy = (x,y)
            # print(pos,txy)

            dim = dir.index(move)
            if path_length[pos][dim] == float("inf"):
                path_length[pos][dim] = unit_path
            else:
                path_length[pos][dim] = (path_length[pos][dim] + unit_path) / 2

            dii = dir.index(opp_moves[move])
            if path_length[txy][dii] == float("inf"):
                path_length[txy][dii] = unit_path
            else:
                path_length[txy][dii] = (path_length[txy][dii] + unit_path) / 2

            pos = txy

    def search_shortest(margin, start, end):
        sx,sy = start
        ex,ey = end
        minx = min(sx,ex); minx = max(0, minx-margin)
        maxx = max(sx,ex); maxx = min(29, maxx+margin)
        miny = min(sy,ey); miny = max(0, miny-margin)
        maxy = max(sy,ey); maxy = min(29, maxy+margin)

        dist = {(i,j):float("inf") for i in range(minx, maxx+1) for j in range(miny,maxy+1)}
        prev = {(i,j):None for i in range(minx, maxx+1) for j in range(miny,maxy+1)}
        LN = 10**20
        que = [(0, start)]
        seen = set()
        # Djikstra
        while que:
            # print(que)
            # print(seen)
            dis, pos = heappop(que)
            seen.add(pos)
            i,j = pos
            ending = False
            for di,(dx,dy) in enumerate(amoves):
                x,y = i+dx,j+dy
                # print(x,y)
                if minx <= x <= maxx and miny <= y <= maxy:
                    txy = (x,y)
                    if txy in seen:
                        continue
                    pld = LN if path_length[pos][di] == float("inf") else path_length[pos][di]
                    pld += dis
                    if pld < dist[txy]:
                        dist[txy] = pld
                        prev[txy] = dir[di]
                        heappush(que, (pld, txy))
                    if txy == end:
                        ending = True
                        break
            if ending:
                break

        # print(prev)
        # Reconstruct
        pos = end
        ans = ""
        while prev[pos]:
            move = prev[pos]
            ans += move
            dx,dy = moves[opp_moves[move]]
            pos = (pos[0]+dx,pos[1]+dy)
        return ans[::-1]

    def search_midest(margin, start, end):
        sx,sy = start
        ex,ey = end
        minx = min(sx,ex); minx = max(0, minx-margin)
        maxx = max(sx,ex); maxx = min(29, maxx+margin)
        miny = min(sy,ey); miny = max(0, miny-margin)
        maxy = max(sy,ey); maxy = min(29, maxy+margin)

        dist = {(i,j):float("inf") for i in range(minx, maxx+1) for j in range(miny,maxy+1)}
        prev = {(i,j):None for i in range(minx, maxx+1) for j in range(miny,maxy+1)}
        LN = -10**20
        que = [(0, start)]
        seen = set()
        # Djikstra
        while que:
            dis, pos = heappop(que)
            seen.add(pos)
            i,j = pos
            ending = False
            for di,(dx,dy) in enumerate(amoves):
                x,y = i+dx,j+dy
                # print(x,y)
                if minx <= x <= maxx and miny <= y <= maxy:
                    txy = (x,y)
                    if txy in seen:
                        continue
                    pld = LN if path_length[pos][di] == float("inf") else path_length[pos][di]
                    pld += dis
                    if pld < dist[txy]:
                        dist[txy] = pld
                        prev[txy] = dir[di]
                        heappush(que, (pld, txy))
                    if txy == end:
                        ending = True
                        break
            if ending:
                break

        # print(prev)
        # Reconstruct
        pos = end
        ans = ""
        while prev[pos]:
            move = prev[pos]
            ans += move
            dx,dy = moves[opp_moves[move]]
            pos = (pos[0]+dx,pos[1]+dy)
        return ans[::-1]

    def search_longest(margin, start, end):
        sx,sy = start
        ex,ey = end
        minx = min(sx,ex); minx = max(0, minx-margin)
        maxx = max(sx,ex); maxx = min(29, maxx+margin)
        miny = min(sy,ey); miny = max(0, miny-margin)
        maxy = max(sy,ey); maxy = min(29, maxy+margin)

        dist = {(i,j):float("inf") for i in range(minx, maxx+1) for j in range(miny,maxy+1)}
        prev = {(i,j):None for i in range(minx, maxx+1) for j in range(miny,maxy+1)}
        LN = -10**20
        que = [(0, start)]
        seen = set()
        # Djikstra
        while que:
            # print(que)
            # print(seen)
            dis, pos = heappop(que)
            seen.add(pos)
            i,j = pos
            ending = False
            for di,(dx,dy) in enumerate(amoves):
                x,y = i+dx,j+dy
                # print(x,y)
                if minx <= x <= maxx and miny <= y <= maxy:
                    txy = (x,y)
                    if txy in seen:
                        continue
                    pld = LN if path_length[pos][di] == float("inf") else path_length[pos][di]
                    pld += dis
                    if pld < dist[txy]:
                        dist[txy] = pld
                        prev[txy] = dir[di]
                        heappush(que, (pld, txy))
                    if txy == end:
                        ending = True
                        break
            if ending:
                break

        # print(prev)
        # Reconstruct
        pos = end
        ans = ""
        while prev[pos]:
            move = prev[pos]
            ans += move
            dx,dy = moves[opp_moves[move]]
            pos = (pos[0]+dx,pos[1]+dy)
        return ans[::-1]

    for case in range(1000):
        sik, sjk, tik, tjk = map(int, input().split())

        percent = []
        percent.append(max(0, int(-0.05*case**2+99)))
        percent.append(max(0, int(-0.0015*(case - 0)**2 + 99)))
        rint = randint(0,100)
        if rint < percent[0]:
            ans = search_longest(0, (sik,sjk), (tik,tjk))
        elif rint < sum(percent):
            ans = search_midest(0,(sik,sjk), (tik,tjk))
        else:
            ans = search_shortest(15,(sik,sjk), (tik,tjk))
        print(ans,flush=True)

        update_path_length(sik, sjk, ans, int(input()), path_length)


if __name__ == '__main__':
    main()
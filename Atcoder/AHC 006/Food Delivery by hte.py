import sys
import random
import math
from time import time
import heapq
# import matplotlib.pyplot as plt

ts = time()
input = sys.stdin.readline
ABCD = [list(map(int, input().split())) for _ in range(1000)]
XY = [(a, b) for a, b, c, d in ABCD]+[(c, d) for a, b, c, d in ABCD]+[(400, 400)]
dist = [[abs(x1-x2)+abs(y1-y2) for x2, y2 in XY] for x1, y1 in XY]

def score(idxs):
    ret = sum([dist[idxs[i]][idxs[i+1]] for i in range(len(idxs)-1)])
    return ret


def get_best_insert_idx(idxs, x):
    # xを入れるbestを探す
    score_min, ret = math.inf, None
    if x<1000:
        for i in range(len(idxs)-1):
            score = dist[idxs[i]][x]+dist[x][idxs[i+1]]-dist[idxs[i]][idxs[i+1]]
            if score<score_min:
                score_min, ret = score, i
            if idxs[i]==x+1000:
                break
    else:
        found = False
        for i in range(len(idxs)-1):
            found = found|(idxs[i]==x-1000)
            if not found:
                continue
            score = dist[idxs[i]][x]+dist[x][idxs[i+1]]-dist[idxs[i]][idxs[i+1]]
            if score<score_min:
                score_min, ret = score, i
    return ret

# 訪問先の入れ替え
# そこそこの初期回
visit_p = set(sorted(range(1000), key=lambda x: max(dist[x][-1], dist[x+1000][-1]))[:50])
kouho = set(sorted(range(1000), key=lambda x: max(dist[x][-1], dist[x+1000][-1]))[50:200])

def cal_score_for_visit_p(visit_p):
    idxs = [-1]
    available = set(visit_p)
    score = 0
    while available:
        min_d, next_i = math.inf, None
        for x in available:
            d =dist[idxs[-1]][x]
            if d < min_d:
                min_d, next_i =d, x
        idxs.append(next_i)
        available.remove(next_i)
        if next_i<1000:
            available.add(next_i+1000)
        score += min_d
    score += dist[idxs[-1]][-1]
    idxs.append(-1)
    return idxs, score


INITIAL_STATE = -5 # Initial position
T = 100 # Temperature
Tmin = 0.0001 # Minimum temperature
COOL = 0.999 # Cooling variable
idxs, cur_score = cal_score_for_visit_p(visit_p)
best_score, best_visit_p = cur_score, set(visit_p)
cnt = 0
while time()-ts<=1.4:
    cnt += 1
    ele_o, ele_n = random.sample(visit_p, 1), random.sample(kouho, 1)
    for ele in ele_o:
        visit_p.remove(ele); kouho.add(ele)
    for ele in ele_n:
        visit_p.add(ele); kouho.remove(ele)
    idxs, new_score = cal_score_for_visit_p(visit_p)
    # print(T, cur_score>new_score, -(cur_score-new_score), -(cur_score-new_score)/T)
    prob = 1 if cur_score>new_score else math.exp((cur_score-new_score)/T)
    if prob==1:#random.random()<prob:
        cur_score = new_score
    else:
        ele_o, ele_n = ele_n, ele_o
        for ele in ele_o:
            visit_p.remove(ele); kouho.add(ele)
        for ele in ele_n:
            visit_p.add(ele); kouho.remove(ele)
    if cur_score < best_score:
        best_score, best_visit_p, best_idxs = cur_score, set(visit_p), list(idxs)
    T = T*COOL

# print(cnt)

"""
beam_s = [(cur_score, visit_p, kouho)]
n_beam, n_haba = 2, 2
while time()-ts<=1.3:
    beam_s_new = list(beam_s)
    for cur_score, visit_p, kouho in beam_s:
        for _ in range(n_haba):
            visit_p = set(visit_p)
            kouho = set(kouho)
            ele_o, ele_n = random.sample(visit_p, 1), random.sample(kouho, 1)
            for ele in ele_o:
                visit_p.remove(ele); kouho.add(ele)
            for ele in ele_n:
                visit_p.add(ele); kouho.remove(ele)
            idxs, new_score = cal_score_for_visit_p(visit_p)
            # print(T, cur_score>new_score, -(cur_score-new_score), -(cur_score-new_score)/T)
            prob = 1 if cur_score>new_score else math.exp((cur_score-new_score)/T)
            if random.random()<prob:
            # if prob==1:
                cur_score = new_score
                beam_s_new.append((cur_score, visit_p, kouho))
            if cur_score < best_score:
                best_score, best_visit_p, best_idxs = cur_score, set(visit_p), list(idxs)
    T = T*COOL
    beam_s = sorted(beam_s_new)[:n_beam]"""

visit_p = best_visit_p
# idxs = best_idxs
# 訪問順序の入れ替え
"""# そこそこの初期回作る
idxs = [-1]
available = set(visit_p)
while available:
    min_d, next_i = math.inf, None
    for x in available:
        d =dist[idxs[-1]][x]
        if d < min_d:
            min_d, next_i =d, x
    idxs.append(next_i)
    available.remove(next_i)
    if next_i<1000:
        available.add(next_i+1000)
idxs.append(-1)
"""
# 貪欲に入れ替え
while time()-ts<1.8:
    ele = random.choice(idxs[1:-1])
    idxs_without_ele = [i for i in idxs if i!=ele]
    i = get_best_insert_idx(idxs_without_ele, ele)
    idxs_without_ele.insert(i+1, ele)
    idxs = idxs_without_ele
# plt.plot(range(len(scores)), scores); plt.show()
print(f"{len(idxs)//2-1} {' '.join(map(lambda x: str(x+1), set([i%1000 for i in idxs if i!=-1])))}")
# print(f"{200} {' '.join(map(lambda x: str(x+1), set([i%1000 for i in  set(sorted(range(1000), key=lambda x: dist[x][-1]+dist[x+1000][-1])[:200]) if i!=-1])))}")
print(f"{len(idxs)} {' '.join(map(lambda i: f'{XY[i][0]} {XY[i][1]}', idxs))}")

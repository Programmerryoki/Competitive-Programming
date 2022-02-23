import itertools
import random
import time
from collections import deque
from copy import deepcopy

random.seed(2)


def search_i(s, field, i, j, N=20):
    for x in range(len(s)):
        if s[x] != field[(i + x) % N][j]:
            return False
    return True


def search_j(s, field, i, j, N=20):
    for x in range(len(s)):
        if s[x] != field[i][(j + x) % N]:
            return False
    return True


def calc_score(field, S, M, N=20):
    cnt = 0
    for z, s in enumerate(S):
        for i in range(N):
            for j in range(N):
                if s[0] == field[i][j]:
                    if search_i(s, field, i, j) or search_j(s, field, i, j):
                        cnt += 1
                        break

            else:
                continue
            break

    return int(cnt / M * 10 ** 8)


def len_check(S):
    """
    20文字よりも長いときはループしているか確認する
    """
    if len(S) > 20:
        for i in range(20, len(S)):
            if S[i - 20] != S[i]:
                return False

    return True


def xyjoin(x, y):
    xlen = -1
    ret = ""
    if x in y:
        return 20, y
    if y in x:
        return 20, x

    for i in range(min(len(x), len(y)) + 1):
        if i > xlen:
            if x[-i:] == y[:i]:
                xlen = i
                ret = x + y[i:]

            if y[-i:] == x[:i]:
                xlen = i
                ret = y + x[i:]

    if len(ret) > 20:
        if len_check(ret):
            ret = ret[:20]
        else:
            xlen = -1
            ret = ""

    return xlen, ret


def joiner(S, zlen):
    nS = deque()
    used = set()
    for x, y in itertools.combinations(S, 2):
        if x in used or y in used:
            continue
        l, s = xyjoin(x, y)
        if l > zlen:
            used.add(x)
            used.add(y)
            nS.append(s)
    for s in S:
        if s not in used:
            nS.append(s)

    return nS


def can_put_h(s, field, ind, i, j, N=20):
    # 方向
    ret = True
    for x in range(N):
        if (
                s[(ind + x) % N] == "."
                or field[(i + x) % N][j] == "."
                or s[(ind + x) % N] == field[(i + x) % N][j]
        ):
            continue
        else:
            ret = False
    if ret:
        for x in range(N):
            if field[(i + x) % N][j] == ".":
                field[(i + x) % N][j] = s[(ind + x) % N]
            else:
                continue
    return ret


def can_put_v(s, field, ind, i, j, N=20):
    # 縦横向
    ret = True
    for y in range(N):
        if (
                s[(ind + y) % N] == "."
                or field[i][(j + y) % N] == "."
                or s[(ind + y) % N] == field[i][(j + y) % N]
        ):
            continue
        else:
            ret = False
    if ret:
        for y in range(N):
            if field[i][(j + y) % N] == ".":
                field[i][(j + y) % N] = s[(ind + y) % N]
            else:
                continue

    return ret


def matcher(s, field, N=20):
    li_i = [z for z in range(N)]
    li_j = [z for z in range(N)]
    random.shuffle(li_i)
    random.shuffle(li_j)

    for i in li_i:
        for j in li_j:
            if field[i][j] != ".":
                ind = s.find(field[i][j])
                if ind == -1:
                    continue
                if (i + j) % 2 == 0:
                    flag = can_put_h(s, field, ind, i, j)
                    if not flag:
                        flag = can_put_v(s, field, ind, i, j)
                else:
                    flag = can_put_v(s, field, ind, i, j)
                    if not flag:
                        flag = can_put_h(s, field, ind, i, j)

                if flag:
                    return True
    else:
        return False


def matcher_allow(s, field, N=20):
    li_i = [z for z in range(N)]
    li_j = [z for z in range(N)]
    random.shuffle(li_i)
    random.shuffle(li_j)

    for i in li_i:
        for j in li_j:
            ind = s.find(field[i][j])
            if ind == -1:
                continue
            if (i + j) % 2 == 0:
                flag = can_put_v(s, field, ind, i, j)
                if not flag:
                    flag = can_put_h(s, field, ind, i, j)

            else:
                flag = can_put_h(s, field, ind, i, j)
                if not flag:
                    flag = can_put_v(s, field, ind, i, j)

            if flag:
                return True
    else:
        return False


def solver(S, start0, start1, N=20):
    field = [["." for _ in range(N)] for _ in range(N)]
    used = [False for _ in range(len(S))]

    # 一番上の行を埋める
    for i, s in enumerate(S[start0]):
        field[0][i] = s
    used[start0] = True

    # 一番左の列を埋める
    i = start1
    while True:
        ind = S[i].find(field[0][0])
        if ind != -1:
            used[i] = True
            break
        else:
            i += 1

    for j in range(20):
        field[j][0] = S[i][(ind + j) % N]

    # 長いものから埋める
    for i in range(len(S)):
        if used[i]:
            continue
        else:
            flag = matcher(S[i], field)
            if flag:
                used[i] = True

    for _ in range(1):
        for i in range(len(S)):
            if used[i]:
                continue
            else:
                flag = matcher_allow(S[i], field)
                if flag:
                    used[i] = True

    return field, used


def juggler(S, z):
    """
    S の後ろの部分をシャッフル
    """
    oS = deepcopy(S)
    oS = oS[int(len(oS) // z) :]
    random.shuffle(oS)
    S[int(len(S) // z) :] = oS

    return S


def main():
    t0 = time.time()
    N, M = map(int, input().split())
    S = [input() for _ in range(M)]
    oS = deepcopy(S)

    for x in range(5, 2, -1):
        for _ in range(3):
            S = joiner(S, x)

    S = sorted(S, key=lambda x: len(x), reverse=True)

    for i in range(len(S)):
        if len(S[i]) < 20:
            S[i] += "." * (20 - len(S[i]))

    t1 = time.time()
    score = -1
    cnt = 0
    while t1 - t0 < 2.7:
        cnt += 1
        field, used = solver(S, random.randint(0, 10), random.randint(0, 10))
        sc = calc_score(field, oS, M, N)
        if sc > score:
            score = sc
            ans = field
        t1 = time.time()
        # if cnt % 4 == 0:
        # S = juggler(S, 1.2)

    for f in ans:
        print("".join(f))


main()

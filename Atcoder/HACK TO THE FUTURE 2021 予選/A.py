from sys import stdin
from time import time
from random import choice, choices
# from copy import deepcopy

def score(move):
    if len(move) > 10000:
        return 0
    s = 4000
    minus = {"U","D","L","R"}
    for i in move:
        if i in minus:
            s -= 1
    return 0 if s <= 0 else s

# def firsttry(positions):
#     st = set([(i[0],i[1]) for i in positions])
#     move = []
#     stack = []
#     for i in range(20):
#         for j in range(20):
#             if i&1:
#                 if j != 0:
#                     move += ["L"]
#                 if (i,20-j-1) in st:
#                     move += ["I"]
#                     stack.append(positions.index([i,20-j-1]))
#             else:
#                 if j != 0:
#                     move += ["R"]
#                 if (i,j) in st:
#                     move += ["I"]
#                     stack.append(positions.index([i,j]))
#         if i != 19:
#             move += ["D"]
#     return sortingandcollect(stack, move)

# def firsttry(positions):
#     st = set([(i[0],i[1]) for i in positions])
#     pos = {i:[] for i in range(20)}
#     for x,y in st:
#         pos[x].append(y)
#     for i in range(20):
#         if i&1:
#             pos[i].sort(key=lambda x: -x)
#         else:
#             pos[i].sort()
#
#     move = []
#     stack = []
#     pm = 0
#     for i in range(20):
#         if i != 19:
#             if i&1:
#                 m = min(pos[i]+pos[i+1])
#             else:
#                 m = max(pos[i]+pos[i+1])
#         else:
#             m = 0
#         # print(pm,m)
#         for j in range(abs(m - pm)+1):
#             if i&1:
#                 rj = pm-j
#                 if j != 0:
#                     move += ["L"]
#                 if (i,rj) in st:
#                     move += ["I"]
#                     stack.append(positions.index([i,rj]))
#                 if rj == m:
#                     move += ["D"]
#                     break
#             else:
#                 rj = j+pm
#                 if j != 0:
#                     move += ["R"]
#                 if (i,rj) in st:
#                     move += ["I"]
#                     stack.append(positions.index([i,rj]))
#                 if rj == m:
#                     move += ["D"]
#                     break
#         pm = m
#     return sortingandcollect(stack, move[:-1])

def firsttry(positions):
    st = set([(i[0],i[1]) for i in positions])
    pos = {i:[] for i in range(20)}
    posi = [[] for i in range(10)]
    for x,y in st:
        pos[x].append(y)
        posi[x//2].append((x,y))
    for i in range(20):
        if i&1:
            pos[i].sort(key=lambda x: -x)
        else:
            pos[i].sort()

    stack = []
    poss = []
    robot = (0,0)
    for i in range(10):
        if i&1:
            card = posi[i]
            while card:
                card.sort(key = lambda x: (abs(robot[0]-x[0])+abs(robot[1]-x[1]), abs(robot[1]-x[1])))
                poss.append([card[0],True])
                stack.append(positions.index(list(card[0])))
                robot = card[0]
                card = card[1:]
            robot = ((i+1)*2,0)
            # if i != 9:
            #     poss.append([robot, False])
        else:
            card = posi[i]
            while card:
                card.sort(key = lambda x: (abs(x[0]-robot[0])+abs(x[1]-robot[1]), abs(x[1]-robot[1])))
                poss.append([card[0],True])
                stack.append(positions.index(list(card[0])))
                robot = card[0]
                card = card[1:]
            robot = ((i+1)*2,19)
            # poss.append([robot,False])
    # print(robot, poss)
    move = movemaker((0,0), poss, [], False)
    return [sortingandcollect(stack, move, poss[-1][0]), stack]

def movemaker(robot, pos, move, pickup):
    # print(pos)
    for (x,y),j in pos:
        dx, dy = x-robot[0],y-robot[1]
        if dx > 0:
            move += ["D"]*dx
        else:
            move += ["U"]*(-dx)
        if dy > 0:
            move += ["R"]*dy
        else:
            move += ["L"]*(-dy)
        if j:
            move += ["IO"[pickup]]
        robot = (x,y)
    return move

def sortingandcollect(stack, move, last):
    pos = []
    for i in stack[::-1]:
        if (i//10)&1:
            pos.append((19 - i//10, 9 - i%10))
        else:
            pos.append((19 - i//10, i%10))
    pos.append((19,0))
    robot = last
    for x,y in pos:
        dx, dy = x-robot[0],y-robot[1]
        if dx > 0:
            move += ["D"]*dx
        else:
            move += ["U"]*(-dx)
        if dy > 0:
            move += ["R"]*dy
        else:
            move += ["L"]*(-dy)
        move += ["O"]
        robot = (x,y)
    move = move[:-1]
    for i in range(19,9,-1):
        move += "I"
        if i&1:
            move += "RI"*9
        else:
            move += "LI"*9
        move += "U"
    # print(move[235:])
    return move[:-1]

def choose(position):
    start = time()
    # print(start)
    stc = []
    mi = []
    mis = 0
    def recur(pos, stack, order, robot):
        nonlocal mi, mis, stc
        if time() - start >= 2.95:
            raise Exception("TLE")
        if len(stack) == 100:
            mvs = sortingandcollect(stack, movemaker((0,0),order,[],False), order[-1][0])
            sc = score(mvs)
            if sc > mis:
                mis = sc
                mi = mvs
                stc = stack
            return
        pos.sort(key=lambda x: (abs(robot[0]-x[0][0])+abs(robot[1]-x[0][1])))
        if len(pos) > 80:
            for i in pos[:1] + [choice(pos[1:])]:
                recur([j for j in pos if j != i], stack+[i[1]], order+[[i[0], 1]],i[0])
        else:
            for i in pos[:1]:
                recur([j for j in pos if j != i], stack+[i[1]], order+[[i[0], 1]],i[0])
    try:
        # print([[position[i], i] for i in range(len(position))])
        recur([[position[i], i] for i in range(len(position))], [], [], (0,0))
        # print("finish")
    except:
        return [mi, mis, stc]

    # def recur(pos, stack, order, robot):
    #     nonlocal mi, mis, stc
    #     if time() - start >= 2.95:
    #         raise Exception("TLE")
    #     if len(stack) == 100:
    #         # print(len(stack),stack)
    #         # print(order)
    #         mvs = sortingandcollect(deepcopy(stack), movemaker((0,0),deepcopy(order),[],False), order[-1][0])
    #         sc = score(mvs)
    #         if sc > mis:
    #             mis = deepcopy(sc)
    #             mi = deepcopy(mvs)
    #             stc = deepcopy(stack)
    #         return
    #     pos.sort(key=lambda x: (abs(robot[0]-x[0][0])+abs(robot[1]-x[0][1])))
    #     if len(pos) > 40:
    #         for i in pos[:1] + [choice(pos)]:
    #             dcpos = deepcopy(pos)
    #             dcpos.remove(i)
    #             recur(dcpos, stack+[i[1]], order+[[i[0], 1]],i[0])
    #     else:
    #         for i in pos[:1]:
    #             dcpos = deepcopy(pos)
    #             dcpos.remove(i)
    #             recur(dcpos, stack+[i[1]], order+[[i[0], 1]],i[0])
    # try:
    #     # print([[position[i], i] for i in range(len(position))])
    #     recur([[position[i], i] for i in range(len(position))], [], [], (0,0))
    #     # print("finish")
    # except:
    #     return [mi, mis, stc]

def file_main():
    from os import listdir
    for fileName in listdir("./Cases"):
        print(fileName)
        start = time()
        positions = []
        with open("./Cases/"+fileName,"r") as file:
            for line in file.readlines():
                positions.append([int(i) for i in line.strip().split()])
        # move, *rest = firsttry(positions)
        # sm = score(move)
        move, mscore, stack = choose(positions)
        print(time()-start)
        # if score(m) < sm:
        #     move = m
        with open("./Ans/"+fileName, "w") as file:
            file.write("".join(move))

def main():
    input = stdin.readline
    position = [[int(i) for i in input().split()] for j in range(100)]
    move, *rest = firsttry(position)
    print(*move, sep="")

def randommain():
    input = stdin.readline
    position = [[int(i) for i in input().split()] for j in range(100)]
    # move, *rest = firsttry(position)
    # sm = score(move)
    move, mscore, stack = choose(position)
    # if score(m) < sm:
    #     move = m
    print(*move, sep="")


if __name__ == "__main__":
    file_main()
    # main()
    # randommain()
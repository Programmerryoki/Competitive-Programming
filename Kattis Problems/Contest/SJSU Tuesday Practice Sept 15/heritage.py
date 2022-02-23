from sys import stdin
input = stdin.readline

N,W = input().split(); N = int(N)
root = [0, {}]
for _ in range(N):
    temp = root
    word, num = input().split(); num = int(num)
    for i in range(len(word)):
        w = word[i]
        if not w in temp:
            temp[1][w] = [0, {}]
        temp = temp[1][w]
        if i == len(word) - 1:
            temp[0] = num

table = [{},0]
dic = root
for w in W:
    nt = [{},0]
    if w in root:
        nt[0][w] = [table[0][w][0],root[w]]

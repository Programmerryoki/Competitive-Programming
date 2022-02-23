from math import ceil

N = int(input())
vote = [int(i) for i in input().split()]
for a in range(N-1):
    ti, ai = [int(i) for i in input().split()]
    if ti != ai:
        mt = ceil(vote[0]/ti)
        ma = ceil(vote[1]/ai)
        vote = [ti*max(mt, ma), ai*max(mt, ma)]
    else:
        vote = [max(vote[0], vote[1]), max(vote[0], vote[1])]
    print(vote[0],vote[1])
print(sum(vote))
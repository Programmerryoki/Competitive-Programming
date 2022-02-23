attri = input().split()
m = int(input())
songs = [input().split() for i in range(m)]
n = int(input())
ans = []
for a in range(n):
    print(" ".join(attri))
    index = attri.index(input())
    songs.sort(key = lambda x : x[index])
    for s in songs:
        print(" ".join(s))
    if a != n-1:
        print()
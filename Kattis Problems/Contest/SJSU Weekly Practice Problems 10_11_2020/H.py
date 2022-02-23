N = int(input())
fw = input()
s = {fw}
for i in range(N-1):
    w = input()
    if w[0] != fw[-1] or w in s:
        print("Player %d lost" % ((i+1)%2+1))
        exit()
    s.add(w)
    fw = w
print("Fair Game")
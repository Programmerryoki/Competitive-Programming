word = "abcdefghijklmnopqrstuvwxyz"
N = int(input())
for a in range(N):
    ans = ""
    line = "".join(input().lower().split())
    for w in word:
        if w not in line:
            ans += w
    if len(ans) == 0:
        print("pangram")
    else:
        print("missing",ans)
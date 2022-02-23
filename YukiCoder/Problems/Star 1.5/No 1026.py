from collections import deque
N = int(input())
string = deque()
for _ in range(N):
    T,S = input().split()
    if T == "0":
        string.append(S)
    else:
        string.appendleft(S)
print("".join(string))
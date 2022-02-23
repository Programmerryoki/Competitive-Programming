N = int(input())
D,X = [int(i) for i in input().split()]
cho = [0]*D
for _ in range(N):
    for i in range(0,D,int(input())):
        cho[i] += 1
print(sum(cho)+X)
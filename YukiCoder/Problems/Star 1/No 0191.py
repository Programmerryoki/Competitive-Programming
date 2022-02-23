N = int(input())
C = [int(i) for i in input().split()]
print(sum([i <= (sum(C)/10) for i in C])*30)
from sys import stdin
input = stdin.readline
W = int(input())
N = int(input())
area = 0
for line in stdin.readlines():
    w,l = map(int, line.strip().split())
    area += int(w)*int(l)
print(area // W)
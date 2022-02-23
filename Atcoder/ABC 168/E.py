N = int(input())
saba = [[int(i) for i in input().split()] for j in range(N)]
grade = {i:set() for i in range(N)}
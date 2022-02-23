point = [sum(list(map(int,input().split(" ")))) for i in range(5)]
print(point.index(max(point))+1,max(point))
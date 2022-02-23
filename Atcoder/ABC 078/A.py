X,Y = [int(i,16) for i in input().split()]
print("<" if X<Y else ">" if X>Y else "=")
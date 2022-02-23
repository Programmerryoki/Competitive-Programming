x,y,z = [int(i) for i in input().split()]
d = abs(x-y)
t = min(x,y)
x,y = x-t,y-t
t += min(z, max(x,y))
z -= min(z, max(x,y))
print(t+z//2)
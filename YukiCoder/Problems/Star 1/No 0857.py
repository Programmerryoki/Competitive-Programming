x,y,z = [int(i) for i in input().split()]
if y <= z:
    z -= 2
elif x <= z:
    z -= 1

print(z)
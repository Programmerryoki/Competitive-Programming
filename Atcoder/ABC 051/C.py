sx,sy,tx,ty = [int(i) for i in input().split()]
t = ""
if sx == tx and sy == ty:

elif sx == tx or sy == ty:

else:
    dx = sx - tx
    dy = sy - ty
    t += "U"*(sy - tx)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

ne = min(a,d)
nf = min(b,c,d)

pos = []
pos.append(ne * e + min(b, c, d-ne) * f)
pos.append(nf * f + min(a,d-nf) * e)
print(max(pos))
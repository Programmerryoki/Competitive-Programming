line = input()
adu = 0
add = 0
adl = 0

t = line[0]
for a in line[1:]:
    if t != a:
        adu += 1
        t = a
    if t != "U":
        adu += 1
        t = "U"

t = line[0]
for a in line[1:]:
    if t != a:
        add += 1
        t = a
    if t != "D":
        add += 1
        t = "D"


t = line[0]
for a in line[1:]:
    if a != t:
        adl += 1
        t = a

print(adu)
print(add)
print(adl)
import enum


class Dire(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3


def debug(i, n):
    command = ["Forward", "Right", "Left"]



def run(l):
    d, x, y = 0, 0, 0
    for a in l:
        #print(a, x, y)
        if a == "Left":
            d = (d+1)%4
        elif a == "Right":
            d = (d+3)%4
        else:
            x = addX(x, d)
            y = addY(y, d)
    return [x, y]


def addX(x, d):
    if d == Dire.east.value:
        return x + 1
    elif d == Dire.west.value:
        return x - 1
    else:
        return x


def addY(y, d):
    if d == Dire.north.value:
        return y + 1
    elif d == Dire.south.value:
        return y - 1
    else:
        return y



x, y = [int(i) for i in input().split()]
n = int(input())
instruction = [input() for i in range(n)]
tx, ty = x-1, y-1
while tx != x and ty != y:
    inst = instruction
    tx, ty = run(inst)
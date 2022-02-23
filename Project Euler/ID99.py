import math
print(math.log(11,2))
print(math.log(11,3))

file = open("ID99_base_exp.txt", "r")
ma = 0
f = file.readlines()
for line in f:
    b, e = [int(i) for i in line[:-1].split(",")]

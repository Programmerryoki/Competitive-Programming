registers = [2,3,5,7,11,13,17,19]
v = [int(i) for i in input().split()]
total = 0
mul = 1
for i in range(len(registers)):
    val = registers[i]
    total += mul * (val-1 - v[i])
    mul *= val
print(total)
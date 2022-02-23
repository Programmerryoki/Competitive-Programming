P = int(input())
mon = [1]*10
for i in range(1,len(mon)):
    mon[i] = mon[i-1] * (i+1)
mon = mon[::-1]
total = 0
for i in range(len(mon)):
    if mon[i] <= P:
        total += P // mon[i]
        P %= mon[i]
print(total)
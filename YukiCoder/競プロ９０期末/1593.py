N = int(input())
count = 0
for x in range(1, N):
    if x**2 > N**2:
        break
    y = round((N**2 - x**2)**0.5)
    # print(x,y)
    if y**2 + x**2 == N**2:
        count += 1
print(count)
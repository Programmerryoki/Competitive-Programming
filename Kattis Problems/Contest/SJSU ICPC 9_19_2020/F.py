dice = list(map(int, input().split()))
output = [0 for i in range(dice[0] + dice[1] + 1)]
for a in range(1, dice[0] + 1):
    for b in range(1, dice[1] + 1):
        output[a + b] += 1

ma = max(output)
for a in range(len(output)):
    if output[a] == ma:
        print(a)
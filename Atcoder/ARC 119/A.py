N = int(input())
mini = float("inf")
pow = 0
n2 = 1
while n2 <= N:
    tp = N // n2
    tmp = pow + tp + (N - n2 * tp)
    if tmp < mini:
        mini = tmp
    pow += 1
    n2 = n2 * 2
print(mini)
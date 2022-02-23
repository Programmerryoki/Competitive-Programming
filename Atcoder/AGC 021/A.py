N = input()
print(max(sum([int(i) for i in N]), 9 * (len(N)-1) + int(N[0]) - 1))
M = [[int(i) for i in input().split()] + [chr(ord("A") + j)] for j in range(3)]
M.sort(key = lambda x: (x[0], -x[1]), reverse=True)
print("\n".join([i[-1] for i in M]))
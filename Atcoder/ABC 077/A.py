grid = [input() for i in range(2)]
print("YES" if grid[0]==grid[1][::-1] else "NO")
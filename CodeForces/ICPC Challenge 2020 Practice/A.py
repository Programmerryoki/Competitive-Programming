file = open("sort.in", "r")
N = int(file.readline())
arr = [int(i) for i in file.readline().split()]
file.close()
arr.sort()
f = open("ans.txt", "w")
f.write(" ".join(map(str, arr)))
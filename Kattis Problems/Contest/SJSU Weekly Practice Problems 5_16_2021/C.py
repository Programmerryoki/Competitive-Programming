A,B,C = sorted(map(int, input().split()))
print(" ".join(map(str, [A if i == "A" else B if i == "B" else C for i in input()])))
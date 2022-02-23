N = int(input())
count = [0]*4
for _ in range(N):
    count[["AC", "WA", "TLE", "RE"].index(input())] += 1
print("AC x",count[0])
print("WA x",count[1])
print("TLE x",count[2])
print("RE x",count[3])
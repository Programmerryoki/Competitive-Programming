# print(927*1.08)
n = int(input())
t = n/1.08
if int(int(t)*1.08) == n:
    print(int(t))
elif int((int(t) + 1)*1.08) == n:
    print(int(t)+1)
else:
    print(":(")
ln = 0
for i in range(100,1000):
    for j in range(100,1000):
        m = i * j
        if str(m) == str(m)[::-1]:
            ln = max(ln, m)
print(ln)
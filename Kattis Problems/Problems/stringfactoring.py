line = input()
for l in range(1,len(line)//2+1):
    for i in range(len(line) - l + 1):
        pat = line[i:i+l]
        if pat[0] != line[i+l]:
            print(pat, " pass")
            continue
        t = pat
        while t == line[i:i+len(t)]:
            t += pat
        line = line[:i] + pat + line[i+len(t)]
        print(line)
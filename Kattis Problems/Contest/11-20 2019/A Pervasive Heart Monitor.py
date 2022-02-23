from sys import stdin
for a in stdin:
    if a == "\n":
        break

    n=a.split()
    hr = 0
    out = []
    for b in n:
        try:
            hr += float(b)
        except:
            out.append(b)
    if hr != 0:
        print(hr / (len(n)-len(out)), end=" ")
    else:
        print(0, end=" ")
    print(" ".join(out))
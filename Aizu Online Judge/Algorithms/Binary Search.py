n = int(input())
s = input().split()
q = int(input())
T = input().split()

def binSearch(a):
    i = n//2
    j = n//2
    done = False
    seen = []
    while True:
        if j != 1:
            j //= 2
        else:
            if i in seen:
                break
            seen.append(i)
        # print(i,j,s[i],a, s[i]==a)
        if s[i] == a:
            return True
        elif s[i] > a:
            i -= j
        else:
            i += j

        if j == 0:
            break
        elif i < 0 or i >= n:
            break
    return False


c = 0
for a in T:
    if binSearch(a):
        c += 1
print(c)
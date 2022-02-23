from collections import Counter

t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    np = 0
    count = Counter()
    pos = False
    for i in range(n):
        # print(count, np)
        av = A[i] + A[n-i-1]
        if i < n//2:
            try:
                count[av] += 1
            except:
                count[av] = 1
        else:
            v, no = count.most_common(1)[0]
            # print(no, n/len(count))
            if no == n/len(count):
                # print("Change")
                pos = True
            if no == n//2:
                if pos:
                    # print(max(count.keys()) - min(count.keys()))
                    if max(count.keys()) - min(count.keys()) <= 2*k:
                        print(min(n//2, np))
                        break
                print(np)
                break

            if av != v:
                if v - A[i] <= k or v - A[n-i-1] <= k:
                    np += 1
                else:
                    np += 2
                count[v] += 1
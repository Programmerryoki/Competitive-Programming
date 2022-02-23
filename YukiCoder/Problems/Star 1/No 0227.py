from collections import Counter
A = [int(i) for i in input().split()]
ac = Counter(A).most_common()
if ac[0][1] == 3:
    if ac[1][1] == 2:
        print("FULL HOUSE")
    else:
        print("THREE CARD")
elif ac[0][1] == 2:
    if ac[1][1] == 2:
        print("TWO PAIR")
    else:
        print("ONE PAIR")
else:
    print("NO HAND")
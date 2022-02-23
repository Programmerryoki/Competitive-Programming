import statistics as st


def means(l):
    if len(l) == 0:
        return 0
    else:
        return st.mean(l)


n = int(input())
deck = [int(i) for i in input().split()]

mean = 0
a = 0
non = False
while a < n:
    # print(deck[:a + 1], deck[a + 1:])
    # print(means(deck[:a + 1]), means(deck[a + 1:]))
    # print()
    if mean <= means(deck[:a + 1]):
        mean = means(deck[:a + 1])
    else:
        break
    a += 1

if mean == 0:
    non = True

if non:
    print(float(0))
else:
    deck2 = deck[a:]
    # print(deck2)
    deck = deck[:a]
    mean = means(deck2)
    # print(mean)
    # print()
    b = 0
    while b < len(deck2) - 1:
        # print(deck2[:b + 1], deck2[b + 1:])
        # print(st.mean(deck2[:b + 1]), st.mean(deck2[b + 1:]))
        # print()
        if mean <= means(deck2[b + 1:]):
            mean = means(deck2[b + 1:])
        else:
            break
        b += 1

    # print(deck, deck2[b:])
    print((sum(deck) + sum(deck2[b:])) / (len(deck) + 1))

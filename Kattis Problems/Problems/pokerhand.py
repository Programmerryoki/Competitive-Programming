import collections
hand = input().split()
card = [i[0] for i in hand]
count = collections.Counter(card)
print(max(count.values()))
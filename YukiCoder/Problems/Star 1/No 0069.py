from collections import Counter
A = input()
B = input()
print("YES") if Counter(A) == Counter(B) else print("NO")
A,B = map(int, input().split())
stth = [2,3,4,5,6,7,8,9,10,11,12,13,1]
print("Alice" if stth.index(A) > stth.index(B) else "Bob" if stth.index(A) < stth.index(B) else "Draw")
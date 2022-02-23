score = input()
A = 0
B = 0
for a in range(0,len(score),2):
    if score[a] == "A":
        A += int(score[a+1])
    else:
        B += int(score[a+1])
if A < B:
    print("B")
else:
    print("A")
print(64**2)
letter = "ABCDEFGH"
for a in range(len(letter)):
    for b in range(1,9):
        for c in range(len(letter)):
            for d in range(1,9):
                print(letter[a], b, letter[c], d)
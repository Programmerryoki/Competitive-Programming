romeTime = ["I","II","III","IIII","V","VI","VII","VIII","IX","X","XI","XII"]
S1, T = input().split()
print(romeTime[(romeTime.index(S1) + int(T))%12])
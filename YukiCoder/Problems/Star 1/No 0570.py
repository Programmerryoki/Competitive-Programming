H = [[int(input()), chr(ord("A") + i)] for i in range(3)]
H.sort(reverse=True)
print("\n".join(map(str, [i[1] for i in H])))
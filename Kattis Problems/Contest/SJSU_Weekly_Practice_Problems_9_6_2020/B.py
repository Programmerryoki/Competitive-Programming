from math import factorial as ft
T = int(input())
print("\n".join(map(str, [str(ft(int(input())))[-1] for i in range(T)])))
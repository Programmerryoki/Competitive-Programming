T, N = [float(i) for i in input().split()]
vegs = [[int(i), 0] for i in input().split()] # list of vegges
vegs.sort()

mass = lambda x: x[0] / (x[1] + 1) #calc the mass
cuts = 0
while mass(vegs[0]) / mass(vegs[-1]) <= T + 0.0001:
    cuts += 1            # count the number of cuts
    vegs[-1][1] += 1     # add cuts to the largest mass ratio?
    vegs.sort(key=mass)  # sort by the mass (initial mass / No of cuts)
print(cuts)
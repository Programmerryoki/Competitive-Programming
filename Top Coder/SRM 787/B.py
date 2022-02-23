from fractions import gcd

class AqaAsadiPlays:
    def getMin(self, A):
        A = list(A)
        A.sort(reverse=True)
        team = [0,A[0]]
        mv = []
        for i in range(len(A)):
            team[0] += A[i]
            team[1] = gcd(team[1], A[i])
            if i+1 < len(A) and team[1] > A[i+1]:
                mv.append(i+1)
        if len(mv) == 0:
            return -1
        return mv[-1]
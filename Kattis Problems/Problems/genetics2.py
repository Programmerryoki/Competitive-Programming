from sys import stdin

def main():
    input = stdin.readline
    N,M,K = map(int, input().split())
    dna = [input() for i in range(N)]
    radix = []
    for i in range(M):
        for j in range(len(dna)):
            if dna[j][i] !=


if __name__ == "__main__":
    main()
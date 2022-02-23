from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def main():
    input = stdin.readline
    T = int(input())
    for _ in range(T):
        n,m = map(int, input().split())
        clauses = []
        used = set()
        order = []
        for _ in range(m):
            tmp = [[],[]]
            line = input().split()
            for i in line:
                if i == "v":
                    continue
                if i[0] == "~":
                    num = int(i[2:])-1
                    tmp[0].append(num)
                else:
                    num = int(i[1:])-1
                    tmp[1].append(num)
                if num not in used:
                    order.append(num)
            clauses.append(tmp)

        def search(i,):
            


        try:
            search()
            temp = False
        except:
            temp = True
        print("satisfiable" if temp else "unsatisfiable")


if __name__ == '__main__':
    main()
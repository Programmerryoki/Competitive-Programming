from functools import lru_cache
from itertools import permutations

def main():
    def over(l,r,rem):
        count = set()
        for L,R in rem:
            if R < l or r <= L:
                continue
            count.add((L,R))
        return count

    def overlap(l,r,rem):
        count = 0
        for L,R in rem:
            if R < l or r <= L:
                continue
            count += 1
        return count

    @lru_cache(None)
    def search():
        return

    def all(ran):
        ans = [0,0]
        for per in permutations(ran, len(ran)):
            rem = set(ran)
            for i,(l,r) in enumerate(per):
                rem -= over(l,r,rem)
                if not rem:
                    break
            ans[i&1] += 1
        return ans


    T = int(input())
    for _ in range(T):
        N = int(input())
        ran = [tuple(int(i) for i in input().split()) for j in range(N)]
        print(ran)
        # if len(ran) > 9:
        #     continue
        print(all(ran))
        # print("Alice" if turn&1 else "Bob")


if __name__ == '__main__':
    main()
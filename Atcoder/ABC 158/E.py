def resolve():
    N, P = [int(i) for i in input().split()]
    S = input()
    count = set()
    c = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            sub = S[i:j]
            if sub in count:
                c += 1
            elif int(sub)%P==0:
                count.add(sub)
                c += 1
    print(c)


import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """4 3
3543"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 2
2020"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """20 11
33883322005544116655"""
        output = """68"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

# from collections import defaultdict
#
# N, P = [int(i) for i in input().split()]
# S = input()
# count = defaultdict(int)
# for i in range(len(S)):
#     for j in range(i+1,len(S)+1):
#         # print(S[i:j])
#         count[S[i:j]] += 1
# c = 0
# for i in count.keys():
#     if int(i)%P==0:
#         c += count[i]
# print(c)
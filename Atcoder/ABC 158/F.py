def resolve():
    N = int(input())
    pos = []
    for _ in range(N):
        X,D = int(input())
        connect = []
        for i,a in enumerate(pos):
            for b in a:
                if X <= b[0] <= X + D:
                    connect.append(i)
                    break
        if len(connect) == 0:
            pos.append([[X,D]])
        else:
            temp = pos[connect[0]]
            for a in connect[1:]:
                if temp[0][]



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
        input = """2
1 5
3 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
6 5
-1 10
3 3"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4
7 10
-10 3
4 3
-4 3"""
        output = """16"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """20
-8 1
26 4
0 5
9 1
19 4
22 20
28 27
11 8
-3 20
-25 17
10 4
-18 27
24 28
-11 19
2 27
-2 18
-1 12
-24 29
31 29
29 7"""
        output = """110"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
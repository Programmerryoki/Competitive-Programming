N = int(input())
heights = [0]*10001
plat = [[int(i) for i in input().split()] for _ in range(N)]
plat.sort()
total = 0
for i in range(N):
    Y,x1,x2 = plat[i]
    total += Y - heights[x1]
    total += Y - heights[x2-1]
    for j in range(x1,x2):
        heights[j] = Y
print(total)

# from math import log2, ceil
#
# class SegTree:
#     def __init__(self,size):
#         self.n = ceil(log2(size))+1
#         self.size = 2**self.n
#         self.bottom = 2**(self.n - 1)
#         self.height = [0]*(self.size)
#         self.data = [0]*(self.size)
#
#     def get_height(self, index):
#         ind = 1; d = 0
#         while d+1 < self.n:
#             if self.data[ind]:
#                 self.height[ind] = max(self.data[ind], self.height[ind])
#                 self.data[ind*2] = self.data[ind]
#                 self.data[ind*2+1] = self.data[ind]
#                 self.data[ind] = 0
#             # print(ind, d, 2**(self.n - d - 2), index, bool(2**(self.n - d - 2) <= index))
#             ind *= 2
#             ind += 2**(self.n - d - 2) <= index
#             d += 1
#         if self.data[ind]:
#             self.height[ind] = max(self.height[ind], self.data[ind])
#             self.data[ind] = 0
#         return self.height[ind]
#
#     def update(self, left, right, val):
#         self._update(0, self.bottom-1, left, right, val)
#
#     def _update(self, l, r, left, right, val):
#         # print(l,r,left,right)
#         if left <= l and r <= right:
#             size = r - l + 1; index = l // size
#             # print(-round(log2(size / self.size))-1, index)
#             self.data[2**(-round(log2(size / self.size))-1) + index] = val
#         elif l <= left and right <= r:
#             self._update(l, (l+r)//2, left, right, val)
#             self._update((l+r)//2+1, r, left, right, val)
#         elif left < l <= right < r:
#             self._update(l, (l+r)//2, left, right, val)
#             if right > (l+r)//2:
#                 self._update((l+r)//2+1, r, left, right, val)
#         elif l < left < r < right:
#             self._update((l+r)//2+1, r, left, right, val)
#             if left < (l+r)//2:
#                 self._update(l, (l+r)//2, left, right, val)
#
#     def __str__(self):
#         string = ""
#         string += "Height :\n"
#         for i in range(self.n):
#             string += (" "*((self.n-i))).join(map(str, self.height[2**i:2**(i+1)]))+"\n"
#         string += "Data :\n"
#         for i in range(self.n):
#             string += (" "*((self.n-i))).join(map(str, self.data[2**i:2**(i+1)]))+"\n"
#         return string
#
#
# N = int(input())
# plat = [[int(i) for i in input().split()] for _ in range(N)]
# plat.sort()
# ST = SegTree(max([max(i[1:]) for i in plat]))
# total = 0
# for i in range(N):
#     y, x1, x2 = plat[i]
#     total += y - ST.get_height(x1-1)
#     total += y - ST.get_height(x2-2)
#     ST.update(x1-1, x2-2, y)
# print(total)
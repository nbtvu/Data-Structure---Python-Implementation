
class DisjointSet(object):
    n = None
    parents = []

    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n

    def find_root(self, i):
        if self.parents[i] < 0:
            return i
        return self.find_root(self.parents[i])

    def merge(self, v1, v2):
        r1 = self.find_root(v1)
        r2 = self.find_root(v2)
        self._merge_roots(r1, r2)

    def _merge_roots(self, r1, r2):
        if self.parents[r1] < self.parents[r2]:
            tmp = self.parents[r2]
            self.parents[r2] = r1
            self.parents[r1] += tmp
        else:
            tmp = self.parents[r1]
            self.parents[r1] = r2
            self.parents[r2] += tmp


ds_1 = DisjointSet(10)

ds_1.merge(1, 3)
ds_1.merge(5, 7)
ds_1.merge(3, 7)

print ds_1.find_root(1)
print ds_1.find_root(3)
print ds_1.find_root(5)
print ds_1.find_root(7)
print ds_1.find_root(9)

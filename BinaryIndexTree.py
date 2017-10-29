
class BIT(object):
    n = None
    tree = None

    def __init__(self, n):
        self.n = n
        self.tree = []

    def get_sum(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum

    def update_element(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += (idx & -idx)
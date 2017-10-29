
class BIT(object):
    n = None
    tree = None

    def __init__(self, n):
        self.n = n
        self.tree = [0]*3*n

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


bit_1 = BIT(1000)
bit_1.update_element(12, 12)
bit_1.update_element(20, 87)
bit_1.update_element(12, -9)

print "Sum from A[1] to A[{0}]: {1}".format(10, bit_1.get_sum(10))
print "Sum from A[1] to A[{0}]: {1}".format(14, bit_1.get_sum(14))
print "Sum from A[1] to A[{0}]: {1}".format(19, bit_1.get_sum(19))
print "Sum from A[1] to A[{0}]: {1}".format(20, bit_1.get_sum(20))
print "Sum from A[1] to A[{0}]: {1}".format(22, bit_1.get_sum(22))

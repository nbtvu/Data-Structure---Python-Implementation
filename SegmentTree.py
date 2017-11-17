class STNode(object):
	def __init__(self, l, r):
		self.left = l
		self.right = r
		self.val = 0

	def __str__(self):
		return str(self.val)

	def __repr__(self):
		return str(self.val)

class MaxNode(STNode):
	def __init__(self, l, r):
		super(MaxNode, self).__init__(l, r)

	@classmethod
	def synthesize(cls, node1, node2):
		if not node1:
			return node2.val
		if not node2:
			return node1.val
		return max(node1.val, node2.val)

	@classmethod
	def synthesize_val(cls, val1, val2):
		if val1 == None:
			return val2
		if val2 == None:
			return val1
		return max(val1, val2)


class MinNode(STNode):
	def __init__(self, l, r):
		super(MinNode, self).__init__(l, r)

	@classmethod
	def synthesize(cls, node1, node2):
		if not node1:
			return node2.val
		if not node2:
			return node1.val
		return min(node1.val, node2.val)

	@classmethod
	def synthesize_val(cls, val1, val2):
		if val1 == None:
			return val2
		if val2 == None:
			return val1
		return min(val1, val2)


class SumNode(STNode):
	def __init__(self, l, r):
		super(SumNode, self).__init__(l, r)

	@classmethod
	def synthesize(cls, node1, node2):
		if not node1:
			return node2.val
		if not node2:
			return node1.val
		return node1.val + node2.val

	@classmethod
	def synthesize_val(cls, val1, val2):
		if val1 == None:
			return val2
		if val2 == None:
			return val1
		return val1 + val2


class SegmentTree(object):
	def __init__(self, n, node_class):
		self.size = n
		self.node_class = node_class
		self.tree = [None]*4*n
		self.pos = [None]*n
		self._initialize_tree(0, 0, n-1)

	def query(self, x, y):
		return self._synthesize(0, x, y)

	def update(self, idx, val):
		pos = self.pos[idx]
		self.tree[pos].val = val
		pos = (pos-1)>>1
		while pos >= 0:
			left_child = self.tree[(pos << 1) + 1]
			right_child = self.tree[(pos << 1) + 2]
			self.tree[pos].val = self.node_class.synthesize(left_child, right_child)
			pos = (pos-1)>>1

	def _initialize_tree(self, pos, l, r):
		self.tree[pos] = self.node_class(l, r)
		if l == r:
			self.pos[l] = pos
			return
		mid = (l+r)/2
		self._initialize_tree((pos << 1) + 1, l, mid)
		self._initialize_tree((pos << 1) + 2, mid+1, r)

	def _synthesize(self, pos, x, y):
		if not self.tree[pos]:
			return None
		if self.tree[pos].left > y or self.tree[pos].right < x:
			return None
		if x <= self.tree[pos].left and self.tree[pos].right <= y:
			return self.tree[pos].val
		left_res = self._synthesize((pos<<1)+1, x, y)
		right_res = self._synthesize((pos<<1)+2, x, y)
		return self.node_class.synthesize_val(left_res, right_res)

segment_tree_1 = SegmentTree(100, node_class=SumNode)
updates = [(1, 2), (3, 19), (23, 52), (42, 1), (58, 32), (17, 29), (19, 10), (10, 100), (32, 28),
		   (22, 28), (3, 19), (6, 111), (43, 12), (78, 12), (87, 1), (46, 69), (99, 11), (0, 2)]
queries = [(0, 99), (2, 18), (45, 99), (23, 78), (2, 12), (38, 90), (46, 47)]

for idx, val in updates:
	segment_tree_1.update(idx, val)

for l, r in queries:
	print l, " -> ", r, ": ", segment_tree_1.query(l, r)

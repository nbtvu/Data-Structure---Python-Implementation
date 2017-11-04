class RBNode(object):
	BLACK = 0
	RED = 1

	def __init__(self, val=None, color=BLACK):
		self.val = val
		self.color = color
		self.left = None
		self.right = None
		self.parents = None

	def is_black(self):
		return self.color == self.BLACK

	def is_red(self):
		return self.color == self.RED

	def flip_color(self):
		self.color = (self.color + 1) % 2

	def color_black(self):
		self.color = self.BLACK

	def color_red(self):
		self.color = self.RED

	def assign_color(self, color):
		self.color = color


class RBTree(object):
	root = None

	def find_val(self, val, start_node=None):
		if not start_node:
			start_node = self.root
		cur = start_node
		while cur and cur.val != val:
			if val > cur.val:
				cur = cur.right
			else:
				cur = cur.left
		return cur

	def find_max_that_less_than_val(self, val, start_node=None):
		if start_node:
			self.root = start_node
		cur = start_node
		res = None
		while cur:
			if cur.val < val:
				res = cur
				cur = cur.right
			else:
				cur = cur.left
		return res

	def find_min_that_greater_than_val(self, val, start_node=None):
		if start_node:
			self.root = start_node
		cur = start_node
		res = None
		while cur:
			if cur.val > val:
				res = cur
				cur = cur.left
			else:
				cur = cur.right
		return res

	def insert_node(self, val):
		if not self.root:
			self.root = RBNode(val, color=RBNode.BLACK)
			return True
		rb_node = RBNode(val, color=RBNode.RED)
		cur = self.root
		while cur:
			if val == cur.val:
				return False
			if val > cur.val:
				if cur.right:
					cur = cur.right
				else:
					cur.right = rb_node
					rb_node.parents = cur
					# do re-coloring
					self.recolor(rb_node)
					break
			else:
				if cur.left:
					cur = cur.left
				else:
					cur.left = rb_node
					rb_node.parents = cur
					# do re-coloring
					self.recolor(rb_node)
					break

	def recolor(self, nd):
		cur = nd
		while cur:
			if cur.is_black():
				return
			if cur == self.root:
				cur.color_black()
				return
			if cur.parents.is_black():
				return
			# at this point, both cur and pa are RED, and grandpa is BLACK
			# do rotating when either pa has no siblings or pa's siblings is BLACK
			pa = cur.parents
			grandpa = pa.parents
			if grandpa.left == pa:
				if not grandpa.right or (grandpa.right and grandpa.right.is_black()):
					if cur == pa.right:
						self._rotate_left(pa)
					grandpa = self._rotate_right(grandpa)
				else:
					pa.color_black()
					grandpa.right.color_black()
					grandpa.color_red()
			else:
				if not grandpa.left or (grandpa.left and grandpa.left.is_black()):
					if cur == pa.left:
						self._rotate_right(pa)
					grandpa = self._rotate_left(grandpa)
				else:
					pa.color_black()
					grandpa.left.color_black()
					grandpa.color_red()
			cur = grandpa


	def delete_node(self, val):
		cur = self.root
		while cur and val != cur.val:
			if val > cur.val:
				cur = cur.right
			else:
				cur = cur.left
		if cur:
			# do remove cur
			return True
		else:
			return False

	def display_tree(self):
		if not self.root:
			print "Empty Tree"
			return
		cur_h = 1
		cur_row = []
		from collections import deque
		nodes_queue = deque()
		nodes_queue.append((self.root, cur_h))
		while nodes_queue:
			cur_node, h = nodes_queue.popleft()
			if h != cur_h:
				print cur_row
				cur_row = []
				cur_h = h
			if not cur_node:
				cur_row = cur_row + [('N', RBNode.BLACK)]
			else:
				cur_row = cur_row + [(cur_node.val, cur_node.color)]
				nodes_queue.append((cur_node.left, h + 1))
				nodes_queue.append((cur_node.right, h + 1))

	def _rotate_left(self, nd):
		tmp = nd.right
		nd.right = tmp.left
		if tmp.left:
			tmp.left.parents = nd
		if nd == self.root:
			tmp.parents = None
			self.root = tmp
		else:
			tmp.parents = nd.parents
			if nd.parents.left == nd:
				nd.parents.left = tmp
			if nd.parents.right == nd:
				nd.parents.right = tmp
		nd.parents = tmp
		tmp.left = nd
		nd_color = nd.color
		nd.assign_color(tmp.color)
		tmp.assign_color(nd_color)
		return tmp

	def _rotate_right(self, nd):
		tmp = nd.left
		nd.left = tmp.right
		if tmp.right:
			tmp.right.parents = nd
		if nd == self.root:
			tmp.parents = None
			self.root = tmp
		else:
			tmp.parents = nd.parents
			if nd.parents.left == nd:
				nd.parents.left = tmp
			if nd.parents.right == nd:
				nd.parents.right = tmp
		nd.parents = tmp
		tmp.right = nd
		nd_color = nd.color
		nd.assign_color(tmp.color)
		tmp.assign_color(nd_color)
		return tmp


rb_tree_1 = RBTree()

a = [13, 1, 9, 12, 98, 34, 32, 12, 28, 7, 6, 65, 14, 123]
for val in a:
	rb_tree_1.insert_node(val)

rb_tree_1.display_tree()

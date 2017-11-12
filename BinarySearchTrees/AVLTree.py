class AVLNode(object):
	val = None
	height = 1
	left = None
	right = None
	parents = None

	def __init__(self, val=None):
		self.val = val


class AVLTree(object):
	root = None

	def find_val(self, val, start_node=None):
		if not start_node:
			start_node = self.root
		cur = start_node
		while (cur and cur.val != val):
			if val < cur.val:
				cur = cur.left
			else:
				cur = cur.right
		return cur

	def find_max_that_less_than_val(self, val, start_node=None):
		if not start_node:
			start_node = self.root
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
		if not start_node:
			start_node = self.root
		cur = start_node
		res = None
		while cur:
			if cur.val > val:
				res = cur
				cur = cur.left
			else:
				cur = cur.right
		return res

	def insert_val(self, val):
		new_node = AVLNode(val)
		cur = self.root
		if not cur:
			self.root = new_node
			return True
		while True:
			if val == cur.val:
				return False
			if val > cur.val:
				if cur.right:
					cur = cur.right
				else:
					cur.right = new_node
					new_node.parents = cur
					self._balance_the_tree(new_node)
					return True
			else:
				if cur.left:
					cur = cur.left
				else:
					cur.left = new_node
					new_node.parents = cur
					self._balance_the_tree(new_node)
					return True

	def remove_val(self, val):
		nd_to_del = self.find_val(val)
		if not nd_to_del:
			return False
		nd_to_swp = self.find_min_that_greater_than_val(val, nd_to_del)
		if not nd_to_swp:
			nd_to_swp = self.find_max_that_less_than_val(val, nd_to_del)

		if not nd_to_swp:
			if not nd_to_del.parents:
				self.root = None
				return True
			if nd_to_del.parents.left == nd_to_del:
				nd_to_del.parents.left = None
			if nd_to_del.parents.right == nd_to_del:
				nd_to_del.parents.right = None
			self._balance_the_tree(nd_to_del.parents)
			return True

		nd_to_del.val = nd_to_swp.val

		if nd_to_swp.left:
			tmp = nd_to_swp.left
		else:
			tmp = nd_to_swp.right
		if nd_to_swp.parents.left == nd_to_swp:
			nd_to_swp.parents.left = tmp
		if nd_to_swp.parents.right == nd_to_swp:
			nd_to_swp.parents.right = tmp
		if tmp:
			tmp.parents = nd_to_swp.parents

		self._balance_the_tree(nd_to_swp.parents)
		return True

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
				cur_row = cur_row + ['N']
			else:
				cur_row = cur_row + [cur_node.val]
				nodes_queue.append((cur_node.left, h + 1))
				nodes_queue.append((cur_node.right, h + 1))

	def _balance_the_tree(self, nd):
		cur = nd
		while cur:
			blnc_factor = self._get_balance_factor(cur)
			if blnc_factor < -1:
				if self._get_balance_factor(cur.right) > 0:
					self._right_rotate(cur.right)
				cur = self._left_rotate(cur)
				cur = cur.parents
				continue
			if blnc_factor > 1:
				if self._get_balance_factor(cur.left) < 0:
					self._left_rotate(cur.left)
				cur = self._right_rotate(cur)
				cur = cur.parents
				continue
			self._update_height(cur)
			cur = cur.parents

	def _left_rotate(self, nd):
		tmp = nd.right
		nd.right = tmp.left
		if tmp.left:
			tmp.left.parents = nd
		tmp.left = nd
		tmp.parents = nd.parents
		nd.parents = tmp
		self._update_parents_link(nd, tmp)
		self._update_height(nd)
		self._update_height(tmp)
		return tmp

	def _right_rotate(self, nd):
		tmp = nd.left
		nd.left = tmp.right
		if tmp.right:
			tmp.right.parents = nd
		tmp.right = nd
		tmp.parents = nd.parents
		nd.parents = tmp
		self._update_parents_link(nd, tmp)
		self._update_height(nd)
		self._update_height(tmp)
		return tmp

	def _get_balance_factor(self, nd):
		if nd.left:
			l_h = nd.left.height
		else:
			l_h = 0
		if nd.right:
			r_h = nd.right.height
		else:
			r_h = 0
		return l_h - r_h

	def _update_height(self, nd):
		if nd.left:
			nd.height = nd.left.height
		else:
			nd.height = 0
		if nd.right:
			if nd.right.height > nd.height:
				nd.height = nd.right.height
		nd.height += 1

	def _update_parents_link(self, old_child, new_child):
		if not new_child.parents:
			self.root = new_child
			return
		if new_child.parents.left == old_child:
			new_child.parents.left = new_child
		else:
			new_child.parents.right = new_child


tree_1 = AVLTree()
val_list = [1, 8, 3, 43, 13, 27, 48, 11, 32, 16, 14, 26, 15, 19, 98, 83, 21, 32, 11, 7, 5, 10]
for val in val_list:
	tree_1.insert_val(val)

# delete a number
tree_1.remove_val(48)

# find smallest number that is greater than 40
print tree_1.find_min_that_greater_than_val(40).val

# find largest number that is less than 40
print tree_1.find_max_that_less_than_val(40).val

# find number 40 in the tree
node = tree_1.find_val(40)
print node.val if node else node

# display the tree
tree_1.display_tree()

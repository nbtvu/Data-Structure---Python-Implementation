from collections import deque

class Node(object):
	def __init__(self, val):
		self.val = val
		self.parents = None
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.val)

	def __repr__(self):
		return str(self.val)

class SplayTree(object):
	def __init__(self):
		self.root = None

	def find_val(self, val):
		cur_node = self.root
		while cur_node and cur_node.val != val:
			if val > cur_node.val:
				cur_node = cur_node.right
			else:
				cur_node = cur_node.left
		return self._splay(cur_node)

	def predecessor(self, val, subtree_root=None):
		if subtree_root:
			cur_node = subtree_root
		else:
			cur_node = self.root
		res = None
		while cur_node:
			if cur_node.val < val:
				res = cur_node
				cur_node = cur_node.right
			else:
				cur_node = cur_node.left
		return self._splay(res)

	def successor(self, val, subtree_root=None):
		if subtree_root:
			cur_node = subtree_root
		else:
			cur_node = self.root
		res = None
		while cur_node:
			if cur_node.val > val:
				res = cur_node
				cur_node = cur_node.left
			else:
				cur_node = cur_node.right
		return self._splay(res)

	def insert_val(self, val):
		if not self.root:
			self.root = Node(val)
			return self.root
		cur_node = self.root
		while cur_node:
			if cur_node.val == val:
				break
			if cur_node.val > val:
				if cur_node.left:
					cur_node = cur_node.left
				else:
					cur_node.left = Node(val)
					cur_node.left.parents = cur_node
					cur_node = cur_node.left
					break
			else:
				if cur_node.right:
					cur_node = cur_node.right
				else:
					cur_node.right = Node(val)
					cur_node.right.parents = cur_node
					cur_node = cur_node.right
					break
		return self._splay(cur_node)


	def delete_val(self, val):
		val_node = self.find_val(val)
		if not val_node:
			return None
		if not self.root.left:
			if not self.root.right:
				# root has no children
				self.root = None
			else:
				# root has only right child
				self.root = self.root.right
				self.root.parents = None
		else:
			if not self.root.right:
				# root has only left child
				self.root = self.root.left
				self.root.parents = None
			else:
				# root has 2 children
				right_child = self.root.right
				self.root = self.root.left
				self.root.parents = None
				self.predecessor(right_child.parents.val)
				self.root.right = right_child
				right_child.parents = self.root
		return val_node

	def display(self):
		if not self.root:
			print "Empty Tree"
			return
		cur_level = 0
		max_level = cur_level
		queue = deque()
		queue.append((self.root, cur_level))
		cur_list = []
		while queue:
			node, level = queue.popleft()
			if level != cur_level:
				if level > max_level:
					break
				print cur_list
				cur_list = []
				cur_level = level
			cur_list.append(node)
			if node:
				queue.append((node.left, level+1))
				queue.append((node.right, level+1))
				max_level = level+1
			else:
				queue.append((None, level+1))
				queue.append((None, level+1))

	def _splay(self, node):
		if not node:
			return None
		pa = node.parents
		while pa:
			grandpa = pa.parents
			if grandpa:
				if pa == grandpa.right and node == pa.left:
					# right - left
					self._right_rotate(pa)
					self._left_rotate(grandpa)
				elif pa == grandpa.left and node == pa.right:
					# left - right
					self._left_rotate(pa)
					self._right_rotate(grandpa)
				elif pa == grandpa.left and node == pa.left:
					# left - left
					self._right_rotate(grandpa)
					self._right_rotate(pa)
				else:
					# right - right
					self._left_rotate(grandpa)
					self._left_rotate(pa)
			else:
				if node == pa.left:
					self._right_rotate(pa)
				else:
					self._left_rotate(pa)
			pa = node.parents
		self.root = node
		return self.root

	def _left_rotate(self, node):
		tmp = node.right
		node.right = tmp.left
		if node.right:
			node.right.parents = node
		tmp.parents = node.parents
		tmp.left = node
		node.parents = tmp
		if tmp.parents:
			if tmp.parents.left == node:
				tmp.parents.left = tmp
			else:
				tmp.parents.right = tmp

	def _right_rotate(self, node):
		tmp = node.left
		node.left = tmp.right
		if node.left:
			node.left.parents = node
		tmp.parents = node.parents
		tmp.right = node
		node.parents = tmp
		if tmp.parents:
			if tmp.parents.left == node:
				tmp.parents.left = tmp
			else:
				tmp.parents.right = tmp


splay_tree = SplayTree()
a = [9, 1, 8, 23, 14, 17, 2, 4, 9, 98, 33, 24, 12, 31, 33, 4, 22]
for val in a:
	splay_tree.insert_val(val)
splay_tree.display()
print splay_tree.find_val(9)
print splay_tree.find_val(32)
print splay_tree.find_val(22)
print splay_tree.delete_val(22)
print splay_tree.find_val(22)
print splay_tree.delete_val(17)
print splay_tree.delete_val(3)
print splay_tree.delete_val(4)
print splay_tree.find_val(33)
print splay_tree.delete_val(33)
print splay_tree.find_val(33)
print splay_tree.insert_val(33)
splay_tree.display()
print splay_tree.find_val(33)

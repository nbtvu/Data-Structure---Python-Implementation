from math import log, ceil
from random import randint

class SLNode(object):
	def __init__(self, val=None, levels=0):
		self.val = val
		self.next_list = [None] * levels

class SkipList(object):
	MAX_LIST_NO = 32
	def __init__(self, max_capacity):
		self.max_level = int(ceil(log(max_capacity, 2)))
		if self.max_level > self.MAX_LIST_NO:
			self.max_level = self.MAX_LIST_NO
		self.max_level -= 1 # since level count from 0
		self.head = SLNode(levels=self.max_level + 1)

	def find_val(self, val):
		cur_level = self.max_level
		cur_node = self.head
		while cur_level >= 0:
			while cur_node.next_list[cur_level] and cur_node.next_list[cur_level].val <= val:
				cur_node = cur_node.next_list[cur_level]
			if cur_node.val == val:
				return cur_node
			cur_level -= 1
		return None


	def predecessor(self, val):
		cur_level = self.max_level
		cur_node = self.head
		while cur_level >= 0:
			while cur_node.next_list[cur_level] and cur_node.next_list[cur_level].val < val:
				cur_node = cur_node.next_list[cur_level]
			cur_level -= 1
		return cur_node


	def successor(self, val):
		cur_level = self.max_level
		cur_node = self.head
		while cur_level >= 0:
			while cur_node.next_list[cur_level] and cur_node.next_list[cur_level].val <= val:
				cur_node = cur_node.next_list[cur_level]
			cur_level -= 1
		return cur_node.next_list[0]


	def insert_val(self, val):
		update_list = self._get_update_list(val)
		new_node = SLNode(val)
		new_node.next_list.append(update_list[0].next_list[0])
		update_list[0].next_list[0] = new_node
		cur_level = 0
		while randint(0,1) and cur_level < self.max_level:
			cur_level += 1
			new_node.next_list.append(update_list[cur_level].next_list[cur_level])
			update_list[cur_level].next_list[cur_level] = new_node


	def delete_val(self, val):
		update_list = self._get_update_list(val)
		target = update_list[0].next_list[0]
		if not target:
			return False
		if target.val != val:
			return False
		for i in range(len(target.next_list)):
			update_list[i].next_list[i] = target.next_list[i]
		return True

	def display_sorted_elements(self):
		cur = self.head.next_list[0]
		res = []
		while cur:
			res.append(cur.val)
			cur = cur.next_list[0]
		print res

	def _get_update_list(self, val):
		update_list = [None] * (self.max_level + 1)
		cur_level = self.max_level
		cur_node = self.head
		while cur_level >= 0:
			while cur_node.next_list[cur_level] and cur_node.next_list[cur_level].val < val:
				cur_node = cur_node.next_list[cur_level]
			update_list[cur_level] = cur_node
			cur_level -= 1
		return update_list


a = [9, 1, 8, 23, 14, 17, 2, 4, 9, 98, 33, 24, 12, 31, 33, 4, 22]
max_capacity = 1234567
skip_list_1 = SkipList(max_capacity)
for val in a:
	skip_list_1.insert_val(val)

print skip_list_1.find_val(17).val
print skip_list_1.successor(17).val
print skip_list_1.predecessor(17).val

skip_list_1.insert_val(19)
skip_list_1.display_sorted_elements()
skip_list_1.insert_val(44)
skip_list_1.display_sorted_elements()
skip_list_1.delete_val(23)
skip_list_1.display_sorted_elements()

print skip_list_1.successor(17).val
print skip_list_1.successor(19).val
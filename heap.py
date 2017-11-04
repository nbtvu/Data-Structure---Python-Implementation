class Heap(object):
	MIN_HEAP = 0
	MAX_HEAP = 1

	def __init__(self, heap_type=MIN_HEAP):
		self.heap_type = heap_type  # 0, 1  <=> min heap, max heap
		self.heap = []
		self.size = 0
		if heap_type == self.MIN_HEAP:
			self.has_higher_priority = self._is_less_than
		else:
			self.has_higher_priority = self._is_greater

	def _is_greater(self, a, b):
		return self.heap[a] > self.heap[b]

	def _is_less_than(self, a, b):
		return self.heap[a] < self.heap[b]

	def insert_val(self, val):
		self.heap.append(val)
		self.size += 1
		self._up_heap(self.size - 1)

	def remove_node_at_pos(self, pos):
		if pos > self.size - 1:
			return False
		self.heap[pos] = self.heap[self.size - 1]
		self.heap.pop()
		self.size -= 1
		self._up_heap(pos)
		self._down_heap(pos)
		return True

	def update_val_at_pos(self, pos, new_val):
		if pos > self.size - 1:
			return False
		self.heap[pos] = new_val
		self._up_heap(pos)
		self._down_heap(pos)
		return True

	def pop_root(self):
		if self.size < 1:
			return None
		res = self.heap[0]
		self.heap[0] = self.heap[self.size - 1]
		self.heap.pop()
		self.size -= 1
		self._down_heap(0)
		return res

	def _up_heap(self, pos):
		if pos > self.size - 1:
			return False
		while pos > 0:
			parents_pos = (pos - 1) / 2
			if self.has_higher_priority(pos, parents_pos):
				self.heap[pos], self.heap[parents_pos] \
					= self.heap[parents_pos], self.heap[pos]
				pos = parents_pos
			else:
				break

	def _down_heap(self, pos):
		if pos > self.size - 1:
			return
		while pos < self.size:
			child = pos * 2 + 1
			if child >= self.size:
				break
			if child + 1 < self.size:
				if self.has_higher_priority(child + 1, child):
					child += 1
			if self.has_higher_priority(child, pos):
				self.heap[child], self.heap[pos] \
					= self.heap[pos], self.heap[child]
				pos = child
			else:
				break

	def display(self):
		if self.size < 1:
			print "Empty Heap"
			return
		max_element = 1
		count = 0
		row = []
		for i in range(self.size):
			row.append(self.heap[i])
			count += 1
			if count == max_element:
				count = 0
				max_element *= 2
				print row
				row = []
		if row:
			print row


h1 = Heap(Heap.MAX_HEAP)
a = [1, 6, 3, 5, 7, 8, 2, 9, 10, 17, 15, 13, 12, 14, 16, 4, 11]
for val in a:
	h1.insert_val(val)

h1.insert_val(13)
h1.pop_root()
h1.update_val_at_pos(6, 26)
h1.remove_node_at_pos(13)
h1.display()

class LinkedListNode(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.pNext = None

class HashFuncs(object):
	# some of good hash functions found here: http://www.cse.yorku.ca/~oz/hash.html
	@classmethod
	def hash_func_djb2(cls, key, modulus):
		if type(key) is not str:
			key = str(key)
		hashed_val = 5381
		for i in range(len(key)):
			hashed_val = (hashed_val << 5) + hashed_val + ord(key[i]) # has = hash * 33 + c
		return hashed_val % modulus
	@classmethod
	def hash_func_sdbm(cls, key, modulus):
		if type(key) is not str:
			key = str(key)
		hashed_val = 0
		for i in range(len(key)):
			hashed_val = \
				ord(key[i]) + (hashed_val << 6) + (hashed_val << 16) - hashed_val # hash * 65599 + key[i]
		return hashed_val % modulus
	@classmethod
	def hash_func_java(cls, key, modulus):
		if type(key) is not str:
			key = str(key)
		hashed_val = 0
		for i in reversed(range(len(key))):
			hashed_val = (hashed_val << 5) - hashed_val + ord(key[i]) # hash = hash * 33 + c
		return hashed_val % modulus

class HashTable(object):
	TAB_SIZE = 1000000
	DJB2 = HashFuncs.hash_func_djb2
	SDBM = HashFuncs.hash_func_sdbm
	JAVA = HashFuncs.hash_func_java
	def __init__(self, hash_func = DJB2, modulus = TAB_SIZE):
		self.hash_func = self._get_hash_func(hash_func)
		self.TAB_SIZE = modulus
		self.hash_table = [None] * modulus

	def map_key_val(self, key, val):
		hashed_val = self.hash_func(key)
		tmp = self.hash_table[hashed_val]
		if not tmp:
			self.hash_table[hashed_val] = LinkedListNode(key, val)
		else:
			while tmp:
				if tmp.key == key:
					tmp.val = val
					return
				tmp = tmp.pNext
			new_node = LinkedListNode(key, val)
			new_node.pNext = self.hash_table[hashed_val]
			self.hash_table[hashed_val] = new_node
		return True

	def  get_val(self, key):
		hashed_val = self.hash_func(key)
		tmp = self.hash_table[hashed_val]
		if not tmp:
			return None
		while tmp:
			if tmp.key == key:
				return tmp.val
			tmp = tmp.pNext
		return None

	def _get_hash_func(self, func):
		def hash_func(key):
			return func(key, self.TAB_SIZE)
		return hash_func

hash_tab_1 = HashTable()
hash_tab_1.map_key_val('hello', 123)
print hash_tab_1.get_val('hello')
hash_tab_1.map_key_val('hello', 999)
print hash_tab_1.get_val('hello')
print hash_tab_1.get_val('how are you')
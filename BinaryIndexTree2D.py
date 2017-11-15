class BIT2D(object):
	def __init__(self, r, c):
		self.n_rows = r
		self.n_cols = c
		self.tree = [[0]*(c+1) for i in range(r+1)]

	def get_sum(self, x1, y1, x2, y2):
		# the origin (0,0) is (bottom-most, left-most) point
		# x1, y1 is (bottom, left) point,
		# x2, y2 is (top, right) point,
		# => sum(x1, y1, x2, y2) = sum(0, 0, x2, y2) + sum(0, 0, x1 - 1, y1 - 1)
		# - sum(0, 0, x2, y1-1) - sum(0, 0, x1-1, y2)
		if x1 > x2 or y1 > y2:
			return None
		if x1 < 1 or y1 < 1:
			return None
		if x2 > self.n_rows or y2 > self.n_cols:
			return None
		return self._get_sum(x2, y2) + self._get_sum(x1 - 1, y1 - 1) \
			   - self._get_sum(x2, y1-1) - self._get_sum(x1-1, y2)

	def add_val(self, x, y, val):
		if x < 1 or y < 1 \
				or x > self.n_rows or y > self.n_cols:
			return
		_x = x
		while _x < self.n_rows:
			_y = y
			while _y < self.n_cols:
				self.tree[_x][_y] += val
				_y = _y + (_y & -_y)
			_x = _x + (_x & -_x)

	def _get_sum(self, x, y):
		if x < 1 or y < 1:
			return 0
		_x = x
		sum = 0
		while _x > 0:
			_y = y
			while _y > 0:
				sum += self.tree[_x][_y]
				_y = _y - (_y & -_y)
			_x = _x - (_x & -_x)
		return sum

m = 1000
n = 1000
bit2d_1 = BIT2D(m, n)
count = 0
for i in range(1,11):
	for j in range(1,11):
		count += 1
		bit2d_1.add_val(i, j, count)

print bit2d_1.get_sum(1,2,2,5)


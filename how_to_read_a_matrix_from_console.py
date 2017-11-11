#read matrix of size MxN
m, n = map(int, raw_input("Input the matrix size (row, column): ").split())
print "Input the matrix elements (row by row): "
a = [None] * m
for i in range(m):
	a[i] = map(int, raw_input().split())

#print out the matrix
print "Print out the matrix:"
for i in range(m):
	line = ""
	for j in range(n):
		line += str(a[i][j])
		line += " "
	print line

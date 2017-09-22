from node import Node
def get_possible_squares(number, node, trees, segments):
	"""
	This method returns all the possible squares where a new queen can be placed give the queens 
	and trees already present.
	"""
	# get the segment number of the node.
	segment = node.segment
	
	# If the segment number of the node is more than the possible segment number, this means that 
	# we have reached the end of the search tree. We no longer have possible places to keep the queen.
	if node.segment > (len(segments.keys()) - 1):
		return []
	
	(start, end) = segments[segment]

	#Initially add all the squares in the segment as possible square. Then start eliminating.
	possible_squares = [(i, start[1]) for i in range(start[0],end[0])]
	
	
	# remove is the set of squares we need to eliminate.
	remove = set()
	append = remove.add
	colno = start[1]
	
	# We iterate over all the queens present and check if any of the squares are attacked by the queens.
	# Remove such squares.
	for queen in node.queens:
		#If a tree is blocking a queen, then the square on the same row is safe.
		# Hence the tree's column number should be greater than that of queen's but lesser than the squares. 
		for tree in trees:
			if (tree[0] == queen[0]) and (tree[1] > queen[1]) and (tree[1] < colno) :
				break
		else:
			append((queen[0],colno))

		# Next check if any of the square is attacked diagonally by the queen.
		# Below the queen.
		x = queen[0]+(colno - queen[1])
		if x < number:
			# Make sure that no tree is blocking the queen fron the square.
			for tree in trees:
				# Ignore all the trees before the queen or after the current square.
				if (tree[1] <= queen[1]) or (tree[1] >= colno):
					continue
				# calculate the area of the triangle - queen, tree, square. If it is zero, then it implies that
				# they are in a straight line.
				area = x*(queen[1] - tree[1]) + queen[0]*(tree[1] - colno) + tree[0]*(colno- queen[1])
				# Tree is blocking. Square is safe.
				if area == 0:
					break
			else:
				# Square is not safe. Add it to the list of squares to be removed.
				append((x,colno))
		# Above the queen
		x = queen[0]-(colno - queen[1])
		if x > -1 :
			# Make sure that no tree is blocking the queen fron the square.
			for tree in trees:
				# Ignore all the trees before the queen or after the current square.
				if (tree[1] <=queen[1]) or (tree[1] >= colno):
					continue
				# calculate the area of the triangle - queen, tree, square. If it is zero, then it implies that
				# they are in a straight line.
				area = x*(queen[1] - tree[1]) + queen[0]*(tree[1] - colno) + tree[0]*(colno- queen[1])
				# Tree is blocking. Square is safe.
				if area == 0:
					break
			else:
				# Square is not safe. Add it to the list of squares to be removed.
				append((x,colno))
	# Remove all the squares that are attacked.
	possible_squares = [ i for i in possible_squares if i not in remove]
	#possible_squares.append(())
	return possible_squares

def expand_frontier( number, node, trees, segments):
	possible_squares = get_possible_squares(number, node, trees, segments)
	l = [ node.copy_node(node.segment+1, square) for square in possible_squares ]
	if node.segment < len(segments.keys()) - 1:
		l.append(node.copy_node(node.segment+1))
	return l

def get_tree_location(arrangement, number):
	return [ (row, column) for column in range(0, number) 
		for row in range (0, number) if arrangement[ row][column] ==2 ]

def dfs_search(number, queens, arrangement, segments):
	if queens > len(segments.keys()):
		return None
	frontier = []
	start = Node(0)
	trees = get_tree_location(arrangement, number)
	frontier += expand_frontier(number, start, trees, segments)
	while len(frontier) > 0:
		node = frontier.pop()
		if len(node.queens) == queens:
			return node
		else:
			frontier+=expand_frontier(number, node, trees, segments)
	return None



from node import Node 
from bfs import bfs_search
from dfs import dfs_search

def write_output(node, arrangement):
	f = open("output.txt", "w")
	if node == None:
		f.write("FAIL\n")
		f.close()
		return
	else:
		f.write("OK\n")
		for x,y in node.queens:
			arrangement[x][y] = 1
		for line in arrangement:
			s = ""
			for i in line:
				s += str(i)
			f.write(s)
			f.write("\n")
		f.close()
		
def print_node(node, arrangement):
	"""
	Print the final output of the program.
	If nothing is returned, that implies that we can't place the given number of queens on the board
	"""
	if node is None:
		print "FAIL"
		return 
	for x,y in node.queens:
		arrangement[x][y] = 1
	for line in arrangement:
		print line

def get_segments(arrangement):
	segments = {}
	count = 0
	for i in range(0, len(arrangement)):
		start = (0,i)
		for j in range(0, len(arrangement)):
			if arrangement[j][i] == 2:
				end = (j,i)
				if start != end:
					segments[count] = [start, end]
					count +=1
					start = (end[0]+1, end[1])
				else:
					start = (end[0]+1, end[1])
				
		end = (len(arrangement), i)
		if start!= end:
			segments[count] = [ start, end]
			count +=1 
	return segments

def read_input():
	f = open("input.txt", "r")
	algorithm = f.readline().strip()
	number = int(f.readline().strip())
	queens = int( f.readline().strip())
	arrangement = [[ int(i) for i in line.strip()] for line in f]
	segments = get_segments(arrangement)
	output = ""
	if algorithm == "DFS":
		output = dfs_search(number, queens, arrangement, segments)
		print_node(output, arrangement)
		write_output(output, arrangement)
	elif algorithm == "BFS":
		output = bfs_search( number, queens, arrangement, segments)
		print_node(output, arrangement)
		write_output(output, arrangement)
	elif algorithm == "SA":
		trees = get_tree_location( arrangement, number)
		output = simulated_annealing(number, queens, arrangement, segments, trees)
		write_sa_output(output)
	
read_input()


	

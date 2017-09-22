"""
The Node data Structure is used to identify a node in the search tree.
Every Node has a number of queens placed on the board during that time.
Additionallu, a segment number is also assoiciated with each node.
A segment can be defined as a continuos area in a column not containing any trees.
A column may have more than one segment.

For example:
000
020
000

In the first column, we have only one segment - 0,0 to 3,0
In the second column, there are 2 segments - 0,1 to 1,1 and 2,1 - 3,1
In the third column there is again only one segment - 0,2 to 3,2
Totally there are 4 segments on the board. 
Every segment can have at 0 or 1 queen in it. 
So we divide the board into segments and start placing the liards on segments.
"""
class Node:
	def __init__(self, segment):
		self.queens = []
		#The co-ordinates of all the queens present on the board
		self.segment = segment
		#The current segment number we are at during the execution of the program
	def append_queens(self, queens):
		self.queens += queens
	def copy_node(self, segment, new_queen=None):
		new = Node(segment)
		if new_queen:
			new.queens = [ queen for queen in self.queens] + [new_queen]
		else:
			new.queens = [ queen for queen in self.queens]
		return new


INFINITY = float('inf')

#class Node():
#	def __init__(self, x, y, distance):
#		self.x = x
#		self.y = y
#		self.distance = distance
		
		
def isInsideGrid(x, y):
	return 0<=x<ROW and 0<=y<COLUMN


# Moves
x = [-1, 0, 1, 0, 1, -1, 1, -1]
y = [0, 1, 0, -1, 1, 1, -1, -1]


def dijkstrasAlgo(mat, ROW, COLUMN):
	# Initialisation 
	queue=[]
	queue.append((mat[0][0], 0, 0))


	dist=[[INFINITY for i in range(COLUMN)] for j in range(ROW)]
	dist[0][0]=mat[0][0]
	
	# visited=[]
	
	while len(queue)!=0:
		curr = heappop(queue)
		
		for i in range(len(x)):
			rows = curr[1] + x[i]
			cols = curr[2] + y[i]
			
			# If the coordinates are valid:
			if isInsideGrid(rows, cols):
				
				# Checks if neighbouring nodes are smaller (or bigger) than the previous node and current node:
				if dist[rows][cols]>dist[curr[1]][curr[2]]+mat[rows][cols]:
					
					# If the distance is not equal to INFINITY, then we remove the node from the queue:
					if dist[rows][cols] != INFINITY:
						queue.remove((dist[rows][cols],rows, cols))

					
					# Update the distance matrix:
					dist[rows][cols]=dist[curr[1]][curr[2]]+mat[rows][cols]
					
					# Append the current node to the queue:
					heappush(queue, (dist[rows][cols],rows, cols))
					
					
		#visited.append((curr.x, curr.y))
		
	return(dist[ROW-1][COLUMN-1])


# Read keyboard input 


import operator
from sys import stdin
from heapq import heappush, heappop

n, m = stdin.readline().split()
n, m = int(n), int(m)
grids=[]

while n!=0 and m!=0:
	mat=[[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		node_value=stdin.readline().strip().split()
		mat[i]=list(map(int, node_value))
	mat.reverse()
	grids.append(mat)
	n, m = stdin.readline().split()
	n, m = int(n), int(m)

for mat in grids:
	ROW=len(mat)
	COLUMN=len(mat[0])
	print(dijkstrasAlgo(mat, ROW, COLUMN))

# BFS implementation from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
from collections import defaultdict
import random

class Graph:
	# every graph object has a hashmap with initial values of empty list
	def __init__(self):
		self.graph = defaultdict(list)

	# function to add edges, by adding vertices to adjacency list
	def addEdge(self, wrestler1, wrestler2):
		self.graph[wrestler1].append(wrestler2)
		self.graph[wrestler2].append(wrestler1)

	# BFS function
	def BFS(self, vertex, array, labels):
		# every vertex starts off as univisited
		visited = defaultdict(None)

		# queue data structure for BFS
		q = []

		# first vertex is put into queue and visited to start off
		q.append(vertex)

		visited[vertex] = True
		labels[vertex] = "Baby Face"

		# as long as the queue is not empty, keep enqueueing and dequeueing
		while q:

			# take out the first vertex FIFO @ index 0
			popped_vertex = q.pop(0)
			array.remove(popped_vertex)

			# examine all the adjacent vertices of dequeued vertex popped_vertex
			for adjacent in self.graph[popped_vertex]:				
				# if never visited, set the visit to True and label it opposite of popped vertex
				if adjacent not in labels:
					visited[adjacent] = True
					if labels[popped_vertex] == "Baby Face":
						labels[adjacent] = "Heel"
					else:
						labels[adjacent] = "Baby Face"
					# add adjacent vertex to queue
					q.append(adjacent)
				
				# if the neighbor has been visited and isn't same as popped vertex, then OK
				elif visited[adjacent] == True and labels[adjacent] != labels[popped_vertex]:
					continue
				
				# if neighbor has been visited and is same as popped vertex, then FALSE
				elif visited[adjacent] == True and labels[adjacent] == labels[popped_vertex]:
					return False, array, labels
		# all trees have been determined to be valid
		return True, array, labels

def main():
	g = Graph()
	#file_name = input("What is your file name? ")
	with open("wrestler2.txt") as file_object:
		
		vertex_count = file_object.readline().strip()
		#print("Vertex count", vertex_count)
		
		wrestler_array = []

		for i in range(int(vertex_count)):
			wrestler_array.append(file_object.readline().strip())
		
		edge_count = file_object.readline().strip()
		#print("Edge count", edge_count)

		for j in range(int(edge_count)):
			# edge read-in
			wrestler1, wrestler2 = file_object.readline().strip().split(" ")
			g.addEdge(wrestler1, wrestler2)

	
	# hashmap to keep track of labels
	labels = defaultdict(None)
	
	my_bool = True

	# keep calling BFS until all vertices have been processed
	while len(wrestler_array) > 0 and my_bool == True:
		my_bool, wrestler_array, labels = g.BFS(random.choice(wrestler_array), wrestler_array, labels)
	
	# if there is at least ONE invalid tree, then everything is invalid
	if my_bool == False:
		print("No")
	# if noting is invalid, then we can print all out labels from our hashmap
	else:
		print("Yes")
		babyfaces = []
		heels = []
		for key, value in labels.items():
			if value == "Baby Face":
				babyfaces.append(key)
			elif value == "Heel":
				heels.append(key)
		print("Babyfaces:", " ".join(babyfaces))
		print("Heels:", " ".join(heels))

if __name__ == '__main__':
	main()


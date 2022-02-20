'''graph1 = {
	'A' : ['B','S'],
	'B' : ['A'],
	'C' : ['D','E','F','S'],
	'D' : ['C'],
	'E' : ['C','H'],
	'F' : ['C','G'],
	'G' : ['F','S'],
	'H' : ['E','G'],
	'S' : ['A','C','G']
}'''

def create_graph():
	graph1={}
	no_of_nodes = int(input("Enter the no. of nodes in the graph : "))
	for i in range(0,no_of_nodes):
		print("----"*16)
		key = input("Enter the node : ") 
		print("For nodes adjacent to {}".format(key)) 

		n = int(input("Enter number of adjacent nodes : "))
		value = []
		# iterating till the range
		print("Enter the nodes : ")
		for i in range(0, n):
			ele = input()
			value.append(ele)
			graph1[key] = value
	return graph1

def dfs(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for k in graph[node]:
			dfs(graph,k,visited)
	return visited

if __name__ =="__main__":
	print("----"*16)
	print("\t"*3,"DFS Traversal")
	print("----"*16)
	graph = create_graph()
	print("----"*16)
	print("The Graph is : {}".format(graph))
	start_node = input("\nEnter the start node : ")
	visited = dfs(graph,start_node, [])
	print("\nThe Depth First Search Traversal is : {}\n".format(visited))
	print("----"*16)

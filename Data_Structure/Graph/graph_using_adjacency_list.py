from collections import defaultdict

# Create a defaultdict to store the adjacency list
graph = defaultdict(list)

# Input the number of vertices and edges
v, e = map(int, input().split())

# Input the edges and populate the adjacency list
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Print the adjacency list
for vertex in graph:
    print(vertex, graph[vertex])

# Get user input and store it in a variable
user_input = input("Please enter something: ")

# Print the user's input
print("You entered:", user_input)

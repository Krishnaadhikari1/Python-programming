def dfs_iterative(graph, start):
    visited = set()      
    stack = [start]         

    while stack:
        vertex = stack.pop() 

        if vertex not in visited:
            print(vertex, end=" ") 
            visited.add(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Depth First Search (using stack) starting from vertex A:")
dfs_iterative(graph, 'A')

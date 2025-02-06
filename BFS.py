from collections import deque
def bfs(graph,start_node):
    visited=set()
    queue=deque([start_node])
    bfs_order=[]
    while queue:
        current_node=queue.popleft()
        
        if current_node not in visited :
            
            visited.add(current_node)
            bfs_order.append(current_node)
            for neighbour in graph[current_node]:
                if neighbour not in visited :
                    queue.append(neighbour)

    return bfs_order
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F', 'G'],
'D': ['B'],
'E': ['B'],
'F': ['C'],
'G': ['C']
}
start_node = 'A'
result = bfs(graph, start_node)
print("BFS traversal order:", result)

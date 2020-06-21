from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []


def bfs(visited, graph, node_name):
    print(node_name, end=' ')
    visited.append(node_name)
    queue.append(node_name)

    while queue:
        node_name = queue.pop()
        for node_name_ in graph[node_name]:
            if node_name_ not in visited:
                print(node_name_, end=' ')
                queue.append(node_name_)
                visited.append(node_name_)


def bfs2(graph, vertex):
    queue = deque([vertex])
    level = {vertex: 0}
    parent = {vertex: None}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in level:
                queue.append(n)
                level[n] = level[v] + 1
                parent[n] = v
    return level, parent

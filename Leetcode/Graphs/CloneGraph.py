"""

"""
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None

    # Dictionary to save the visited node and it's respective clone
    # as key and value respectively. This helps to avoid cycles.
    visited = {}

    q = deque()
    q.append(node)

    visited[node] = Node(node.val, [])

    #BFS traversal
    while q:
        curr = q.popleft()

        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val, [])
                q.append(neighbor)
            # Add the clone of the neighbor to the neighbors of the clone node "n".
            visited[curr].neighbors.append(visited[neighbor])


    return visited[node]

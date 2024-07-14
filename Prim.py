import heapq

def prim(vertices, edges):
    mst = []
    visited = set()

    # Create a dictionary of adjacency lists
    adj = {v: [] for v in vertices}
    for u, v, weight in edges:
        adj[u].append((weight, u, v))
        adj[v].append((weight, v, u))

    # Start from the first vertex
    start_vertex = vertices[0]
    min_heap = adj[start_vertex]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for edge in adj[v]:
                if edge[2] not in visited:
                    heapq.heappush(min_heap, edge)

    return mst


# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 5),
    ('C', 'E', 4),
    ('D', 'E', 2),
    ('D', 'F', 3),
    ('E', 'F', 3)
]

mst = prim(vertices, edges)
print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(edge)

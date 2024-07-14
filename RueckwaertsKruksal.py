class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def backwards_kruskal(vertices, edges):
    mst = []
    disjoint_set = DisjointSet(vertices)

    # Sort edges based on weight in descending order
    edges.sort(key=lambda x: x[2], reverse=True)

    # Initially, add all edges to the MST
    mst = edges[:]

    for edge in edges:
        u, v, weight = edge

        # Check if removing the current edge will disconnect the graph
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
        else:
            mst.remove(edge)

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

mst = backwards_kruskal(vertices, edges)
print("Edges in the Maximum Spanning Tree:")
for edge in mst:
    print(edge)

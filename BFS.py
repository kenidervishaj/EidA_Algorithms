graph = {
    '5' : ['3', '7'],  # 5 is parent node, 3 and 7 are its kids
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = []  # list for visited nodes
queue = []  # the queue for the nodes

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    # visited = 5
    # queue = 5

    while queue:
        m = queue.pop(0)

        # queue = []

        print (m, end = " ")  # 5

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                    # visited = [5, 3, 7]
                queue.append(neighbour)


print("Following is the Breadth-First-Search")
bfs(visited, graph, '5')
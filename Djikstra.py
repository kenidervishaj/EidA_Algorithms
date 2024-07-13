import heapq
def djikstra(graph, start):
    # priority queue to store distance, vertex tuples
    priority_queue = [(0, start)]

    #Dictionary to store the shortest path to each vertex
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    #Dictionariy to store the previous vertex in the optimal path
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        # remove the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        #skip processing if the distance in the queue is not up to date
        if current_distance > shortest_paths[current_vertex]:
            continue

        #explore nighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # only consider this path if its better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return  shortest_paths, previous_vertices

# Adjacency List
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_paths, previous_vertices = djikstra(graph, 'A')

print("Shortest path: ", shortest_paths)
print("Previous vertices: ", previous_vertices)
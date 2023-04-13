# calculating eigen vector centrality

import numpy as np

# define the adjacency matrix of the graph
adj_matrix = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

# compute the principal eigenvector of the adjacency matrix
eigenvalues, eigenvectors = np.linalg.eig(adj_matrix)

principal_eigenvector = eigenvectors[:, np.argmax(eigenvalues)]

# normalize the eigenvector to obtain the eigenvector centrality of the nodes
eigenvector_centrality = principal_eigenvector / np.sum(principal_eigenvector)

print("Eigenvector centrality:", eigenvector_centrality)

import queue
import graphs

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    q = queue.PriorityQueue()
    q.put((0, id(start), start))

    while not q.empty():
        current_distance, _, current_node = q.get()

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                q.put((distance, id(neighbor), neighbor))

    return distances

# graph=graphs.Romenia()
# graph.add()
# graph=graph.romenia.graph


# start="Oradea"
# print(dijkstra(graph,start))
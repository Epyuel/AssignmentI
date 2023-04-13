import graphs
from Search_algorithms import Algorithms
import numpy
class Centralities:
    def degree(self,graph,start):
        degree=len(graph[start])
        return degree

    def closeness(self,graph,start,decimal_place=10):
        algorithm=Algorithms()
        total_costs,paths=algorithm.dijkstra(graph,start)
        closeness=(len(graph)-1)/(sum(total_costs[city] for city in total_costs ))
        return numpy.round(closeness,decimal_place)
    
    def betweenness(self,graph,start,decima_place=10):
        algorithm=Algorithms()
        paths_through_start=0
        lis_paths=[]
        for city in graph:
            if city==start:
                continue
            total_costs,paths=algorithm.dijkstra(graph,city)
            del paths[start]
            lis_paths+=sum(paths.values(),[])
            paths_through_start+=lis_paths.count(start)
        n=len(graph)
        #Here this is the total number of paths except for start
        total_paths=(n-1)*(n-2)/2
        betweenness=paths_through_start/total_paths
        return numpy.round(betweenness,decima_place)
        
    def eigen_vector(self,graph,start,decimal_place=10):
        new_graph,nodes=self.list_to_matrix(graph)
        eigenvalues, eigenvectors = numpy.linalg.eig(new_graph)
        principal_eigenvector = eigenvectors[:, numpy.argmax(eigenvalues)]
        # normalize the eigenvector to obtain the eigenvector centrality of the nodes
        eigenvector_centrality = principal_eigenvector / numpy.sum(principal_eigenvector)
        return numpy.round(eigenvector_centrality[nodes.index(start)],decimal_place)
    
    # This method converts adjecency list to adjacency matrix to compute eigen vector
    def list_to_matrix(self,adj_list):
        nodes=list(adj_list.keys())
        adj_matrix= numpy.zeros((len(adj_list),len(adj_list)))

        for i,node in enumerate(nodes):
            for j in adj_list[node]:
                adj_matrix[i][nodes.index(j[0])]=1
        return adj_matrix,nodes

# graph=graphs.Romenia()
# graph.add()
# graph=graph.romenia.graph
# start="Sibiu"
# c=Centralities()
# print(c.closeness(graph,start))

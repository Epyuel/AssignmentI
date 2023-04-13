from centralities import Centralities
import graphs
graph=graphs.Romenia()
graph.add()
graph=graph.romenia.graph
central=Centralities()
centralities={}
with open("romenia_locations.txt","r") as file:
    for line in file:
        if line.startswith("City"):
            continue
        line_lis=line.split()
        city=" ".join(line_lis[:-2])
        print(f"{city}:\n  Between: {central.betweenness(graph,city)}, Close: {central.closeness(graph,city)}, Degree: {central.degree(graph,city)}, Eigen: {central.eigen_vector(graph,city)}\n")

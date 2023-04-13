# For this specific assignment,Nodes aren't considered to be alone(with out edges).
class Node:
    def __init__(self,data):
        self.data=data
        self.heuristics=None
    
class Graph(dict):
    def __init__(self):
        self.graph={}
    def add(self,node1,node2,cost):
        node1=Node(node1)
        node2=Node(node2)
        if node1.data in self.graph and node2.data not in self.graph:
            self.graph[node1.data].append((node2.data,cost))
            self.graph[node2.data]=[(node1.data,cost)]
        elif node2.data in self.graph and node1.data not in self.graph:
            self.graph[node2.data].append((node1.data,cost))
            self.graph[node1.data]=[(node2.data,cost)]
        elif node1.data not in self.graph and node2.data not in self.graph:
            self.graph[node1.data]=[(node2.data,cost)]
            self.graph[node2.data]=[(node1.data,cost)]
        else:
            self.graph[node1.data].append((node2.data,cost))
            self.graph[node2.data].append((node1.data,cost))

    def add_only_node(self,node):
        self.graph[node]=[]

    def remove_node(self,node):
        node=Node(node)
        if node.data in self.graph:
            for i in self.graph[node.data]:
                self.graph[i[0]].remove((node.data,i[1]))
            del self.graph[node.data]
        else:
            print(f"{node.data} doesn't exist in the graph")

    def remove_edge(self,node1,node2):
        node1=Node(node1)
        node2=Node(node2)
        for i in self.graph[node1.data]:
            if i[0]==node2.data:
                self.graph[node1.data].remove((i[0],i[1]))
                break
        for i in self.graph[node2.data]:
            if i[0]==node1.data:
                self.graph[node2.data].remove((i[0],i[1]))
        else:
            print(f"There is no path between {node1.data} and {node2.data}")

        


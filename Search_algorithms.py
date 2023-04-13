import heapq
import itertools
import time
from collections import deque
from numpy import sin, cos, arccos, pi, round

# In the Algorithms class dfs method(implemented using recursion) make use of the class property,
# hence in the driver code it is mandatory to use different instances(objects) of the class.
class Algorithms:
    def dfs(self,graph,start,goal,heuristics=None):
        visited={}
        parent=None
        frontier=[]
        path=deque()
        frontier.append([start,None])  
        while frontier:
            current=frontier.pop()
            if current[0] not in visited:
                visited[current[0]]=current[1]
                current[1]=current[0]
            if current[0]==goal:
                break
            for city in graph[current[0]]:
                if city[0] not in visited:
                    frontier.append([city[0],current[1]])
        if goal not in visited:
            return []
        parent=goal
        while parent:
            path.appendleft(parent)
            parent=visited[parent]
        return path

    def ucs(self,graph,start,goal,heuristics=None):
        parent=None
        visited={}
        frontier=[]
        frontier.append((start,0))
        path=deque()
        while frontier:
            frontier=sorted(frontier,key= lambda x:x[1],reverse=True)
            current=frontier.pop()
            if current[0]==goal:
                break
            if current[0] not in visited:
                visited[current[0]]=(parent,current[1])
            parent=current
            for i in graph[current[0]]:
                if i[0] not in visited:
                    visited[i[0]]=(parent[0],i[1])
                    frontier.append((i[0],i[1]+parent[1]))
        if goal in visited:
            curr=visited[goal]
        else:
            return []
        path.appendleft(goal)
        while curr[0]!=None:
            path.appendleft(curr[0])
            curr=visited[curr[0]]
        return path
            
    def a_star(self,graph,start,goal,heuristics):
        parent=None
        visited={}
        frontier=[]
        frontier.append((start,heuristics[start]))
        path=deque()
        while frontier:
            frontier=sorted(frontier,key= lambda x:x[1],reverse=True)
            current=frontier.pop()
            if current[0]==goal:
                break
            if current[0] not in visited:
                visited[current[0]]=(parent,current[1])
            parent=current
            for i in graph[current[0]]:
                if i[0] not in visited:
                    visited[i[0]]=(parent[0],i[1])
                    frontier.append((i[0],i[1]+parent[1]+heuristics[i[0]]))
        if goal in visited:
            curr=visited[goal]
        else:
            return []
        path.appendleft(goal)
        while curr[0]!=None:
            path.appendleft(curr[0])
            curr=visited[curr[0]]
        return path

    def heuristc_fun(self,start,goal):
        #Read the locations from romenia_locations.txt  file and store it in dictionary.
        line_dict={}
        with open("romenia_locations.txt","r") as file:
            for line in file:
                if line.startswith("City"):
                    continue
                line_lis=line.split()
                line_dict[" ".join(line_lis[:-2])]=(float(line_lis[-2]),float(line_lis[-1]))
        #Iterate over the line_dict and produce the distance in miles between two locations.
        latitude=(line_dict[start][0],line_dict[goal][0])
        longitude=(line_dict[start][1],line_dict[goal][1])
        theta = longitude[0] - longitude[1]
        distance = 60 * 1.1515 * arccos(round(
                (sin(latitude[0]*pi/180) * sin(latitude[1]*pi/180)) + 
                (cos(latitude[0]*pi/180) * cos(latitude[1]*pi/180) * cos(theta*pi/180)),8))*180/pi
        distance=round(distance,2)
        return distance

    def dijkstra(self,graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        paths = {node: [start] for node in graph}
        visited = {}
        p_queue = [(0, 0, start)]
        tiebreaker = itertools.count()

        while p_queue:
            (dist, _, curr_node) = heapq.heappop(p_queue)
            if curr_node in visited:
                continue
            visited[curr_node] = True
            for (neigh_node, weight) in graph[curr_node]:
                if neigh_node not in visited:
                    new_dist = dist + weight
                    if new_dist < distances[neigh_node]:
                        distances[neigh_node] = new_dist
                        paths[neigh_node] = paths[curr_node] + [neigh_node]
                        heapq.heappush(p_queue, (new_dist, next(tiebreaker), neigh_node))

            for (prev_node, weight) in graph[curr_node]:
                if prev_node not in visited:
                    new_dist = dist + weight
                    if new_dist < distances[prev_node]:
                        distances[prev_node] = new_dist
                        paths[prev_node] = paths[curr_node] + [prev_node]
                        heapq.heappush(p_queue, (new_dist, next(tiebreaker), prev_node))
        return distances, paths
    # This function will take any algorithm with their start and goal; run it n number of times and return-
    # the average time in MicroSeconds and their solution length.
    def average_calc(self,algorithm,graph,start,goal,n):
        heuristics={}
        with open("romenia_locations.txt","r") as file:
            for line in file:
                if line.startswith("City"):
                    continue
                line_lis=line.split()
                city_name=' '.join(line_lis[:-2])
                heuristics[city_name]=self.heuristc_fun(city_name,goal)        
        total_time=0 
        for i in range(n):

            start_instance=time.perf_counter()
            path=algorithm(graph,start,goal,heuristics)
            end_instance=time.perf_counter()

            span=(end_instance-start_instance)*1000000
            total_time+=span
        avg_time=round(total_time/n,2)
        if (algorithm==self.dfs):
            print(f"DFS Algorithm\n Start:{start}\n Goal:{goal}")
            print(f"Average_time:{avg_time} MicroSeconds\nPath_length:{len(path)}\nPath:{path}\n")
        elif(algorithm==self.ucs):
            print(f"UCS Algorithm\n Start:{start}\n Goal:{goal}")
            print(f"Average_time:{avg_time} MicroSeconds\nPath_length:{len(path)}\nPath:{path}\n")
        elif(algorithm==self.a_star):
            print(f"A* Search Algorithm\n Start:{start}\n Goal:{goal}")
            print(f"Average_time:{avg_time} MicroSeconds\nPath_length:{len(path)}\nPath:{path}\n")

# Driver code:

# graph={"a":[("b",5),("c",4)],"b":[("d",2),("a",5),("c",7)],"c":[("a",4),("b",7)],"d":[("b",2),("e",1)],"e":[("d",1)],"f":[]}
# heuristics={"a":7,"b":3,"c":1,"d":1,"e":0,"f":4}
# start="a"
# goal="e"
# dfs=Algorithms()

# # dfs.dfs(graph,start,goal)
# # print(dfs.path[::-1])

# # print(dfs.ucs(graph,start,goal,heuristics))
# print(dfs.dfs(graph,start,goal))

# # print(dfs.a_star(graph,start,goal,heuristics))
# # print(dfs.heuristc_fun("Pitesti","Pitesti"))


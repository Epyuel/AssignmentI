import graphs
import Search_algorithms as sa
graph=graphs.Romenia()
graph.add()
graph=graph.romenia.graph
algo=sa.Algorithms()
start="Zerind"
goal="Eforie"
print(algo.dfs(graph,start,goal))


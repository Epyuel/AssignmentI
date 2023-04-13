import graphs
import Search_algorithms as sa
# The romenia graph we populated on the 'graphs.py'.
graph=graphs.Romenia()
graph.add()
graph=graph.romenia.graph
selected_cities=["Oradea","Timisoara","Rimnicu Vilcea","Pitesti","Fagaras","Eforie","Bucharest","Arad","Urziceni","Vaslui"]
for start in selected_cities:
    for goal in selected_cities:
        if start==goal:
            continue
        fagaras=sa.Algorithms()
        final_solution1=fagaras.average_calc(fagaras.dfs,graph,start,goal,100000)
        final_solution1
        final_solution2=fagaras.average_calc(fagaras.ucs,graph,start,goal,100000)
        final_solution2
        final_solution3=fagaras.average_calc(fagaras.a_star,graph,start,goal,100000)
        final_solution3